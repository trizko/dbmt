import psycopg2
import os
import argparse

class MigrationTool:
    def __init__(self, db_config, migrations_dir):
        self.db_config = db_config
        self.migrations_dir = migrations_dir
        self.connection = psycopg2.connect(**self.db_config)
        self.cursor = self.connection.cursor()
        self._ensure_migrations_table()

    def _ensure_migrations_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS migrations (
                id SERIAL PRIMARY KEY,
                name TEXT UNIQUE,
                applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.connection.commit()

    def get_applied_migrations(self):
        self.cursor.execute("SELECT name FROM migrations ORDER BY id")
        applied_migrations = [row[0] for row in self.cursor.fetchall()]
        return applied_migrations

    def apply_migration(self, migration_name):
        with open(os.path.join(self.migrations_dir, migration_name), 'r') as file:
            sql = file.read()

        self.cursor.execute(sql)
        self.cursor.execute("INSERT INTO migrations (name) VALUES (%s)", (migration_name,))
        self.connection.commit()

    def rollback_migration(self, migration_name):
        downgrade_file = migration_name.replace('.sql', '_down.sql')
        downgrade_path = os.path.join(self.migrations_dir, downgrade_file)

        if not os.path.exists(downgrade_path):
            print(f"No downgrade script found for {migration_name}")
            return

        with open(downgrade_path, 'r') as file:
            sql = file.read()

        self.cursor.execute(sql)
        self.cursor.execute("DELETE FROM migrations WHERE name = %s", (migration_name,))
        self.connection.commit()

    def migrate(self):
        applied_migrations = self.get_applied_migrations()
        all_migrations = sorted(os.listdir(self.migrations_dir))

        for migration in all_migrations:
            if migration not in applied_migrations and not migration.endswith('_down.sql'):
                print(f"Applying migration: {migration}")
                self.apply_migration(migration)
                print(f"Migration applied: {migration}")

    def downgrade(self):
        applied_migrations = self.get_applied_migrations()
        if not applied_migrations:
            print("No migrations to roll back")
            return

        last_migration = applied_migrations[-1]
        print(f"Rolling back migration: {last_migration}")
        self.rollback_migration(last_migration)
        print(f"Migration rolled back: {last_migration}")

def main():
    parser = argparse.ArgumentParser(description="PostgreSQL Migration Tool")
    subparsers = parser.add_subparsers(dest="command")

    up_parser = subparsers.add_parser("up", help="Run migrations")
    down_parser = subparsers.add_parser("down", help="Rollback last migration")

    args = parser.parse_args()

    db_config = {
        'dbname': 'your_db_name',
        'user': 'your_db_user',
        'password': 'your_db_password',
        'host': 'your_db_host',
        'port': 'your_db_port'
    }
    migrations_dir = "migrations"

    tool = MigrationTool(db_config, migrations_dir)

    if args.command == "up":
        tool.migrate()
    elif args.command == "down":
        tool.downgrade()

if __name__ == "__main__":
    main()