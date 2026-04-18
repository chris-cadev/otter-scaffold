# FastAPI + HTMX Scaffold Template

A Copier template for creating FastAPI + HTMX + Tailwind CSS projects with production-ready patterns.

## Usage

### Prerequisites

Install Copier:

```bash
pip install copier
# or: uv tool install copier
```

### Generate a New Project

```bash
copier copy gh:chriscadev/py-wscaffold my-project
```

Or with a specific version:

```bash
copier copy gh:chriscadev/py-wscaffold@v2.0.0 my-project
```

Or from GitLab:

```bash
copier copy git+https://repos.chrislabs.net/chriscadev/scaffold my-project
```

### Options

During project creation, you'll be prompted for:

| Option                 | Default         | Description                        |
| ---------------------- | --------------- | ---------------------------------- |
| `project_name`         | my-app          | Project name                       |
| `package_name`         | my_app          | Python package name                |
| `author_name`          | Your Name       | Author name                        |
| `author_email`         | you@example.com | Author email                       |
| `include_htmx`         | true            | Include HTMX for dynamic HTML      |
| `include_auth`         | false           | Include JWT authentication         |
| `database`             | postgres        | Database backend (sqlite/postgres) |
| `include_docker`       | true            | Include Docker configuration       |
| `include_alembic`      | true            | Include Alembic migrations         |
| `include_rate_limiting`| false           | Include slowapi rate limiting      |
| `include_error_pages`  | false           | Include custom HTML error pages    |
| `include_e2e`         | false           | Include Playwright e2e tests       |
| `port`                 | 9091            | Development server port            |

### Update Existing Project

```bash
cd my-project
copier update
```

## Features

- **FastAPI** with async SQLAlchemy
- **HTMX** + Tailwind CSS + daisyUI for dynamic frontend
- **PostgreSQL** with connection pooling (default)
- **Service/Controller** architecture pattern
- **Alembic** migrations
- **Docker** and Docker Compose support
- **Rate limiting** (optional)
- **Custom error pages** (optional)
- **E2E tests** with Playwright (optional)

## Development

```bash
# Install dependencies
pdm install

# Install client dependencies
pdm run client_install

# Build frontend
pdm run build

# Run migrations
pdm run migrate

# Start development server
pdm run dev

# Run tests
pdm run test

# Run e2e tests (if enabled)
pdm run e2e
```

## Database Commands

```bash
# Start PostgreSQL
pdm run db_up

# Stop PostgreSQL
pdm run db_down

# View database logs
pdm run db_logs

# Backup database
pdm run backup

# Restore database
pdm run restore <backup_file>
```

## Deployment

```bash
# Full deploy (backup, sync, build, migrate, restart)
pdm run deploy

# Docker compose commands
pdm run dc_build    # Build Docker image
pdm run dc_up       # Start services
pdm run dc_down     # Stop services
pdm run dc_migrate  # Run migrations in container
```

## Architecture

```
src/{{ package_name }}/
├── app.py                    # FastAPI application entry point
├── core/                     # Shared utilities
│   ├── config.py             # Configuration (DATABASE_URL, SITE_URL)
│   ├── database.py           # SQLAlchemy async engine & session
│   ├── responses.py          # Jinja2 templates
│   └── filters.py            # Custom Jinja2 filters
├── features/                 # Feature modules
│   └── hello/                # Example feature
│       ├── routes.py         # FastAPI router
│       ├── models.py         # SQLAlchemy models
│       ├── controllers/      # Controller (handles templates/responses)
│       └── services/         # Business logic with dataclass I/O
└── migrations/               # Alembic migrations
```

## Hosting

Template repository: https://repos.chrislabs.net/chriscadev/scaffold