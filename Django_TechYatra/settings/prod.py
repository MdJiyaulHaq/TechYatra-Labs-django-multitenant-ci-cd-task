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
