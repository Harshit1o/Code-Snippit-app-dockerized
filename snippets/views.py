from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.utils import timezone
from .models import CodeSnippet
from .serializers import CodeSnippetSerializer

# Create your views here.

class CodeSnippetViewSet(viewsets.ModelViewSet):
    serializer_class = CodeSnippetSerializer

    def get_queryset(self):
        # Only return non-expired snippets
        return CodeSnippet.objects.filter(expiry_date__gt=timezone.now())

    def perform_create(self, serializer):
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class HomeView(ListView):
    model = CodeSnippet
    template_name = 'snippets/home.html'
    context_object_name = 'snippets'
    paginate_by = 9

    def get_queryset(self):
        return CodeSnippet.objects.filter(expiry_date__gt=timezone.now()).order_by('-created_at')

class CreateSnippetView(CreateView):
    model = CodeSnippet
    template_name = 'snippets/create_snippet.html'
    fields = ['title', 'code', 'language', 'expires_in']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'Snippet created successfully!')
        return super().form_valid(form)

class SnippetDetailView(DetailView):
    model = CodeSnippet
    template_name = 'snippets/snippet_detail.html'
    context_object_name = 'snippet'

    def get_queryset(self):
        return CodeSnippet.objects.filter(expiry_date__gt=timezone.now())

def delete_snippet(request, pk):
    snippet = get_object_or_404(CodeSnippet, pk=pk)
    if request.method == 'POST':
        snippet.delete()
        messages.success(request, 'Snippet deleted successfully!')
        return redirect('home')
    return redirect('snippet_detail', pk=pk)
