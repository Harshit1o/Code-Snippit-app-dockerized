from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CodeSnippetViewSet,
    HomeView,
    CreateSnippetView,
    SnippetDetailView,
    delete_snippet
)

router = DefaultRouter()
router.register(r'snippets', CodeSnippetViewSet, basename='api_snippet')

urlpatterns = [
    # API URLs
    path('api/', include(router.urls)),
    
    # Template URLs
    path('', HomeView.as_view(), name='home'),
    path('create/', CreateSnippetView.as_view(), name='create_snippet'),
    path('snippet/<int:pk>/', SnippetDetailView.as_view(), name='snippet_detail'),
    path('snippet/<int:pk>/delete/', delete_snippet, name='delete_snippet'),
] 