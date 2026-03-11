# App

FastAPI + HTMX + Tailwind CSS boilerplate with SQLite, daisyUI, and WebSocket support.

## Quick Start

```bash
# Install dependencies
pdm install
pdm run client_install
pdm run build

# Run migrations
pdm run migrate

# Start development server
pdm run dev
```

Visit http://localhost:9091

## Features

- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - Async ORM with SQLite
- **HTMX** - Dynamic HTML without JavaScript
- **Tailwind CSS v4** - Utility-first CSS
- **daisyUI** - Component library for Tailwind
- **Alembic** - Database migrations

## Development

```bash
# Watch mode for frontend
pdm run watch

# Run tests
pdm run test

# Create new migration
pdm run migration_create "your message"
```

## Production

```bash
# Build and run with Docker
docker-compose up --build
```
