import os
import django
import time

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'code_expiry.settings')
django.setup()

from snippets.models import CodeSnippet
from django.utils import timezone

def cleanup_expired_snippets():
    while True:
        # Delete expired snippets
        expired = CodeSnippet.objects.filter(expiry_date__lte=timezone.now())
        if expired.exists():
            count = expired.count()
            expired.delete()
            print(f"Deleted {count} expired snippet(s)")
        
        # Wait for 1 hour
        time.sleep(3600)

if __name__ == '__main__':
    print("Starting cleanup service...")
    cleanup_expired_snippets() 