# TechYatra-Labs Django Multi-Tenant Application with CI/CD

This repository contains a multi-tenant Django application using [django-tenants](https://django-tenants.readthedocs.io/), PostgreSQL, and Docker. It is fully integrated with GitHub Actions for CI/CD, enabling automated testing, linting, and Docker image publishing.
Developed as part of the Django Developer technical task for TechYatra Labs.

---

## Project Overview

This project demonstrates a scalable SaaS-style architecture using PostgreSQL schemas for tenant isolation. Each tenant has its own schema, while shared data resides in the public schema. The application is containerized for easy deployment and leverages GitHub Actions for continuous integration and delivery.

---

## Features

- Multi-tenancy using `django-tenants` with PostgreSQL schemas.
- Example tenant-specific app: **products** (e.g., each tenant has isolated products).
- Example shared app: **customers** (public schema, manages tenants).
- Dockerized with a multi-stage build for small, secure images.
- Local development and testing with Docker Compose.
- GitHub Actions CI/CD:
  - Automated testing (`pytest`)
  - Linting (`flake8`)
  - Docker image build and push to GHCR on version tags.
- Semantic versioning (MAJOR.MINOR.PATCH).
- Environment-based configuration (development/production).

---

## Repository Structure

```
├── Django_TechYatra/         # Django project root
│   ├── settings/             # Settings (base, dev, prod)
│   └── ...
├── customers/                # Shared app (public schema)
├── products/                 # Tenant-specific app
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── requirements.dev.txt
├── .env.example
├── .github/
│   └── workflows/            # CI/CD workflows
└── README.md
```

---

## Setup Instructions

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) & Docker Compose
- (Optional) Python 3.13+ locally for direct execution

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/TechYatra-Labs-django-multitenant-ci-cd-task.git
cd TechYatra-Labs-django-multitenant-ci-cd-task
```

### 2. Configure Environment Variables

Copy the example env file and edit as needed:

```bash
cp .env.dev .env.dev
# (edit .env.dev to set POSTGRES_USER, POSTGRES_PASSWORD, SECRET_KEY, etc.)
```

### 3. Build and Run with Docker Compose

```bash
docker compose up --build
```

This will start both the Django app and a PostgreSQL database. The app will be available at [http://localhost:8000](http://localhost:8000).

---

## Creating Tenants

Tenants are managed via the `customers` app (public schema). To create a new tenant:

1. **Enter the web container shell:**
   ```bash
   docker compose exec web bash
   ```
2. **Create a tenant with Django shell:**
   ```bash
   python manage.py shell
   ```
   ```python
   from customers.models import Client, Domain
   tenant = Client(schema_name='tenant1', name='Tenant 1', paid_until='2030-01-01', on_trial=True)
   tenant.save()
   domain = Domain(domain='tenant1.localhost', tenant=tenant, is_primary=True)
   domain.save()
   ```
3. **Access the tenant:**
   Visit `http://tenant1.localhost:8000` (see `/etc/hosts` if needed for local dev).

---

## Running Tests and Linting

**Lint code:**

```bash
docker compose run --rm web flake8
```

**Run tests:**

```bash
docker compose run --rm web bash -c "python manage.py migrate_schemas --shared && pytest"
```

---

## CI/CD Workflows

CI/CD is powered by GitHub Actions:

- **Linting and Testing:**
  On every push or PR to `main`, runs flake8 and pytest in containers (`.github/workflows/linting-and-testing.yml`).

- **Docker Build (CI):**
  On every push or PR to `main`, builds the Docker image to verify Docker compatibility (`.github/workflows/ci.yml`).

- **Release (Publish to GHCR):**
  On every push of a tag like `v1.2.3`, builds and pushes the Docker image to GitHub Container Registry as both `:v1.2.3` and `:latest` (`.github/workflows/release.yml`).

---

## Versioning

This project uses [Semantic Versioning](https://semver.org/) (MAJOR.MINOR.PATCH).
Release a new version by pushing a tag like `v1.0.0` to GitHub.

---

## Production Deployment Notes

- Use `.env.prod` for production secrets and DB credentials.
- Set `DJANGO_SETTINGS_MODULE=Django_TechYatra.settings.prod` in production.
- Use a reverse proxy (e.g., Nginx) for SSL and domain routing.
- Set proper `ALLOWED_HOSTS` and enable HTTPS-related settings in `prod.py`.
- Consider persistent storage (volumes) for media/static and Postgres data.
- Scale with Docker Compose, Kubernetes, or your preferred orchestrator.

---

## Technology Stack

- Python 3.13+
- Django 5.x
- [django-tenants](https://django-tenants.readthedocs.io/) (PostgreSQL schemas)
- PostgreSQL
- Docker & Docker Compose
- GitHub Actions (CI/CD)

---

## License

This project is licensed under the MIT License. See [LICENSE](./LICENSE) for details.
