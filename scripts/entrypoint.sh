#!/bin/bash

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Start Celery worker for background tasks (if needed in the future)
# celery -A code_expiry worker --loglevel=info &

# Start the cleanup cron job in the background
while true; do
    echo "Running cleanup of expired snippets..."
    python manage.py cleanup_expired
    sleep 3600  # Sleep for 1 hour
done &

# Start server
echo "Starting server..."
python manage.py runserver 0.0.0.0:8000 