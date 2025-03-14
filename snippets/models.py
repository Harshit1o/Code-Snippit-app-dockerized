from django.db import models
from django.utils import timezone
from datetime import timedelta

class CodeSnippet(models.Model):
    EXPIRY_CHOICES = [
        (1, '1 Hour'),
        (24, '1 Day'),
        (168, '1 Week'),
    ]

    title = models.CharField(max_length=100)
    code = models.TextField()
    language = models.CharField(max_length=50, default='python')
    created_at = models.DateTimeField(auto_now_add=True)
    expires_in = models.IntegerField(choices=EXPIRY_CHOICES, default=24)
    expiry_date = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.expiry_date:
            self.expiry_date = timezone.now() + timedelta(hours=self.expires_in)
        super().save(*args, **kwargs)

    def is_expired(self):
        return timezone.now() >= self.expiry_date

    def __str__(self):
        return f"{self.title} (Expires: {self.expiry_date})"

    class Meta:
        ordering = ['-created_at']
