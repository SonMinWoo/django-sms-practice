from django.urls import path
from snippets import views

urlpatterns = [
    path('auth/', views.auth_post),
    path('auth/verify/', views.verify_post),
]