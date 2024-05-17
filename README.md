# dbmt

`dbmt` is a simple PostgreSQL migration tool written in Python. It helps you manage database migrations, including applying new migrations and rolling back the last applied migration.

## Features

- Apply new migrations
- Rollback the last applied migration
- Keep track of applied migrations

## Requirements

- Python 3.x

## Installation

Install `dbmt` from the root directory of this repo:

```sh
pip install .
```

## Usage

### Subcommands

- `up`: Apply new migrations.
- `down`: Rollback the last applied migration.

### Command-line Arguments

- `--db-url`: The PostgreSQL database URL (required).
- `--migrations-dir`: The directory containing migration files (default: `migrations`).

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