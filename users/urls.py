from django.urls import path, include
from .views import Me

urlpatterns = [
    path("me/", Me.as_view()),
]
