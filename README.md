# FastAPI + HTMX Scaffold Template

A Copier template for creating FastAPI + HTMX + Tailwind CSS projects.

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

Or from GitLab:

```bash
copier copy git+https://repos.chrislabs.net/chriscadev/scaffold my-project
```

### Options

During project creation, you'll be prompted for:

| Option            | Default         | Description                        |
| ----------------- | --------------- | ---------------------------------- |
| `project_name`    | my-fastapi-app  | Project name                       |
| `package_name`    | (auto)          | Python package name                |
| `author_name`     | Your Name       | Author name                        |
| `author_email`    | you@example.com | Author email                       |
| `include_htmx`    | true            | Include HTMX for dynamic HTML      |
| `include_auth`    | false           | Include JWT authentication         |
| `database`        | sqlite          | Database backend (sqlite/postgres) |
| `include_docker`  | true            | Include Docker configuration       |
| `include_alembic` | true            | Include Alembic migrations         |
| `port`            | 9091            | Development server port            |

### Update Existing Project

```bash
cd my-project
copier update
```

## Development

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

## Hosting

Template repository: https://repos.chrislabs.net/chriscadev/scaffold
