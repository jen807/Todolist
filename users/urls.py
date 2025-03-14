from django.urls import path, include

# from .views import Me, Signup
from . import views

urlpatterns = [
    path("me/", views.Me.as_view()),
    path("signup/", views.Signup.as_view()),
    path("login/", views.Login.as_view()),
    path("logout/", views.Logout.as_view()),
    path("change-password/", views.ChangePassword.as_view()),
    # path("edit/", views.Edit.as_view()),
]
