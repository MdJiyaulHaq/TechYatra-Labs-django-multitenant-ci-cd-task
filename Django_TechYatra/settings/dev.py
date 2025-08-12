from .base import *

DEBUG = True
ALLOWED_HOSTS = ["*"]  # for local development

DATABASES["default"].update(
    {
        "HOST": "db",  # Docker Compose service name for Postgres
        "USER": "postgres",
        "PASSWORD": "strongpassword",
    }
)
