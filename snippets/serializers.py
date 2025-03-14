from rest_framework import serializers
from .models import CodeSnippet

class CodeSnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeSnippet
        fields = ['id', 'title', 'code', 'language', 'created_at', 'expires_in', 'expiry_date']
        read_only_fields = ['created_at', 'expiry_date'] 