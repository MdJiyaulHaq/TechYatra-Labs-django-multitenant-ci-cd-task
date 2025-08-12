from .base import *

DEBUG = False
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "my-domain.com", "www.my-domain.com"]

DATABASES["default"].update(
    {
        "HOST": os.getenv("POSTGRES_HOST", "db"),
        "USER": os.getenv("POSTGRES_USER", "postgres"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", "strongpassword"),
        "NAME": os.getenv("POSTGRES_DB", "postgres"),
    }
)

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
