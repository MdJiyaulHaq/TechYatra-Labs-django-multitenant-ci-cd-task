# TechYatra-Labs-Django Multi-Tenant Application with CI/CD

This repository contains a multi-tenant Django application using [django-tenants](https://django-tenants.readthedocs.io/), containerized with Docker and uses PostgreSQL, and integrated with GitHub Actions for CI/CD.  
Developed as part of the Django Developer technical task for Techyatralabs.

---

## Features
- Multi-tenancy using `django-tenants` with PostgreSQL schemas
- Example tenant-specific model: **Product**
- Dockerized setup with multi-stage build for optimized image size
- Local development with `docker-compose`
- GitHub Actions CI pipeline:
  - Run tests
  - Lint code (flake8)
  - Build Docker image
  - Push Docker image to Github Container Registry on version tags
- Semantic versioning (MAJOR.MINOR.PATCH)

---

## Getting Started

### Prerequisites
- Docker & Docker Compose
- Python 3.13+

### Local Setup (Docker Compose)
```bash
# Clone the repo
git clone https://github.com/<your-username>/TechYatra-Labs-django-multitenant-ci-cd-task.git
cd TechYatra-Labs-django-multitenant-ci-cd-task

# Copy environment variables template
cp .env.example .env

# Build & run containers
docker-compose up --build
