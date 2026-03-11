# Deployment Guide

This guide covers deploying the boilerplate with Docker and Cloudflare Tunnel.

## Prerequisites

- Docker and Docker Compose
- Cloudflare account with a domain
- Bun (for frontend build)

## Quick Start

### 1. Clone and Configure

```bash
# Clone the boilerplate
git clone <your-repo> my-app
cd my-app

# Copy environment template
cp .env.example .env
```

### 2. Configure Environment

Edit `.env`:

```bash
JWT_SECRET=your-secure-random-string
SITE_URL=https://your-domain.com
DATABASE_URL=sqlite+aiosqlite:///app.db
```

Generate a secure JWT secret:
```bash
openssl rand -hex 32
```

### 3. Install Dependencies

```bash
# Install Python dependencies
pdm install

# Install Node dependencies
pdm run client_install

# Build frontend assets
pdm run build
```

### 4. Run Database Migrations

```bash
pdm run migrate
```

### 5. Build and Run with Docker

```bash
docker compose up --build -d
```

The app will be available at `http://localhost:9091`

## Cloudflare Tunnel Setup

### 1. Run Cloudflare Commands

All cloudflared commands can be run from the Docker container:

```bash
docker compose run --rm cloudflare ...
```

### 2. Login to Cloudflare

```bash
docker compose run --rm cloudflare tunnel login
```

This will open a browser window to authenticate with Cloudflare.

### 3. Create a Tunnel

```bash
docker compose run --rm cloudflare tunnel create app_tunnel
```

Save the tunnel ID - you'll need it for configuration.

### 4. Create Cloudflare DNS Record

```bash
# Point your domain to the tunnel
docker compose run --rm cloudflare tunnel route dns app_tunnel your-domain.com
```

### 5. Configure Tunnel

Create `cloudflared/config.yml`:

```yaml
tunnel: <tunnel-id>
ingress:
  - hostname: your-domain.com
    service: http://app:9091
  - service: http_status:404
```

### 6. Update docker-compose.yml

The tunnel container expects credentials at:
```
./cloudflare/volumes:/home/nonroot/.cloudflared
```

Mount your credentials:
```bash
mkdir -p .cloudflare/volumes
cp ~/.cloudflared/<tunnel-id>.json .cloudflare/volumes/credentials.json
```

### 7. Restart Services

```bash
docker compose down
docker-compose up -d
```

Your app should now be accessible at `https://your-domain.com`

## Adding New Features

### Create a New Feature

```bash
# Copy the hello feature as a template
cp -r src/app/features/hello src/app/features/your_feature

# Update the files:
# - models.py (your database models)
# - services.py (database queries)
# - routes.py (API endpoints)
# - templates/*.html (your UI)
```

### Register the Feature

In `src/app/app.py`:

```python
from app.features.your_feature.routes import router as your_feature_router

# Add to app
app.include_router(your_feature_router)
```

### Add Frontend Assets

In `vite.config.js`, add your entry point:

```javascript
input: {
  main: './src/app/core/client/main.ts',
  hello: './src/app/features/hello/client/main.ts',
  your_feature: './src/app/features/your_feature/client/main.ts',
}
```

## Production Checklist

- [ ] Set strong `JWT_SECRET`
- [ ] Configure `SITE_URL` to your domain
- [ ] Enable HTTPS via Cloudflare
- [ ] Set up database backups
- [ ] Configure log rotation
- [ ] Set up health checks

## Troubleshooting

### App Won't Start

Check logs:
```bash
docker-compose logs app
```

### Database Issues

Reset the database:
```bash
docker-compose exec app pdm run drop_db
docker-compose exec app pdm run migrate
```

### Tunnel Connection Issues

Check tunnel logs:
```bash
docker-compose logs cloudflare
```

Verify credentials:
```bash
ls -la .cloudflare/volumes/
```
