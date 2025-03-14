from django.core.management.base import BaseCommand
from django.utils import timezone
from snippets.models import CodeSnippet

class Command(BaseCommand):
    help = 'Deletes all expired code snippets'

    def handle(self, *args, **kwargs):
        expired_snippets = CodeSnippet.objects.filter(expiry_date__lte=timezone.now())
        count = expired_snippets.count()
        expired_snippets.delete()
        self.stdout.write(
            self.style.SUCCESS(f'Successfully deleted {count} expired snippet(s)')
        ) 