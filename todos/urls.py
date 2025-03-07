from django.urls import path, include
from .views import Todos

urlpatterns = [
    path("", Todos.as_view()),
]
