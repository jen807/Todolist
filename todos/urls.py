from django.urls import path, include

# from .views import Todos
from . import views

urlpatterns = [
    path("", views.Todos.as_view()),
    path("<int:pk>", views.TodoDetail.as_view()),
]
