#!/bin/sh
set -e

# Wait for Postgres to become available (uses psycopg2, so ensure it's in requirements.txt)
echo "Waiting for Postgres..."

python - <<'PY'
import os, time, sys
import psycopg2
from psycopg2 import OperationalError
host = os.getenv("POSTGRES_HOST", "db")
port = os.getenv("POSTGRES_PORT", "5432")
db = os.getenv("POSTGRES_DB", "postgres")
user = os.getenv("POSTGRES_USER", "postgres")
password = os.getenv("POSTGRES_PASSWORD", "strongpassword")

dsn = f"host={host} dbname={db} user={user} password={password} port={port}"
for i in range(60):
    try:
        conn = psycopg2.connect(dsn)
        conn.close()
        print("Postgres is up")
        sys.exit(0)
    except OperationalError:
        print("Postgres not ready, sleeping 1s...")
        time.sleep(1)
print("Postgres still not available after waiting")
sys.exit(1)
PY

# Run shared migrations
echo "Applying shared migrations..."
python manage.py migrate_schemas --shared

# If running production settings, collectstatic
if [ "$DJANGO_SETTINGS_MODULE" = "Django_TechYatra.settings.prod" ]; then
  echo "Collecting static files..."
  python manage.py collectstatic --noinput
fi

# exec the container CMD
exec "$@"