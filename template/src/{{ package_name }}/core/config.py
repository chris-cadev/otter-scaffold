from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()

{% if database == 'sqlite' %}
DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite+aiosqlite:///{{ package_name }}.db")
{% elif database == 'postgres' %}
DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql+asyncpg://postgres:postgres@localhost:5432/{{ package_name }}")
{% endif %}
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is required")
if not DATABASE_URL.startswith("sqlite+aiosqlite://") and not DATABASE_URL.startswith("postgresql+asyncpg://"):
    raise ValueError(
        "DATABASE_URL must compatible with either SQLite or PostgreSQL"
    )

SITE_URL = os.environ.get("SITE_URL", "http://localhost:{{ port }}")

{% if include_auth %}
JWT_ALGORITHM = "HS256"
JWT_SECRET = os.environ.get("JWT_SECRET")
if not JWT_SECRET:
    raise ValueError("JWT_SECRET environment variable is required")
{% endif %}
