# dbmt

`dbmt` is a simple PostgreSQL database migration tool written in Python. It helps you manage database migrations, including applying new migrations and rolling back the last applied migration.

## Features

- Apply new migrations
- Rollback the last applied migration
- Keep track of applied migrations

## Requirements

- Python 3.x

## Installation

This package is not uploaded to PyPi but can be installed from this repository's URL in the following ways:

### Using `pip`
Install directly from the command line using pip, like so:
```sh
pip install git+https://github.com/trizko/dbmt
```
Or by adding it to your `requirements.txt`:
```
dbmt @ git+https://github.com/trizko/dbmt
```

### Using `poetry`
With poetry, you can install by adding the following to your `pyproject.toml`:
```toml
[tool.poetry.dependencies]
dbmt = { git = "https://github.com/trizko/dbmt.git" }
```

## Usage

### Subcommands

- `up`: Apply new migrations.
- `down`: Rollback the last applied migration.

### Command-line Arguments

- `--db-url`: The PostgreSQL database URL (required).
- `--migrations-dir`: The directory containing migration files (default: `migrations`).

### Migration file naming
When creating migration files, consider the following rules of how these files are applied during upgrades and downgrades:
- Migration files are applied in alphanumerical order. It is recommended that they use a number prefix and a descriptive name for the migration, e.g. `001_initial.sql`, `002_add_users_table.sql`, etc.
- The downgrade files should have the same number prefix and description as the upgrade files, followed by the `_down` suffix, e.g. `001_initial_down.sql`, `002_add_users_table_down.sql`, etc. These files will only be used during downgrades.

### Examples

#### Applying Migrations

To apply all pending migrations:

```sh
dbmt up --db-url postgres://user:password@localhost:5432/your_db_name --migrations-dir migrations
```

#### Rolling Back the Last Migration

To rollback the last applied migration:

```sh
dbmt down --db-url postgres://user:password@localhost:5432/your_db_name --migrations-dir migrations
```

### Migration Files

Create your migration files in the specified migrations directory. Use a consistent naming convention, such as `001_initial.sql`, `002_add_users_table.sql`, etc.

Each migration file should contain valid SQL commands for the migration. For example:

**`001_initial.sql`**
```sql
CREATE TABLE example (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);
```

**`001_initial_down.sql`**
```sql
DROP TABLE example;
```

**`002_add_users_table.sql`**
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
```

**`002_add_users_table_down.sql`**
```sql
DROP TABLE users;
```

### Contributing

Contributions are welcome. Please submit a pull request or open an issue to discuss any changes.

### License

This project is licensed under the MIT License. See the LICENSE file for details.