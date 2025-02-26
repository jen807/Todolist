from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUser(UserAdmin):
    fieldsets = (
        (
            "프로필",
            {
                "fields": (
                    "username",
                    "password",
                    "email",
                    "avatar",
                    "name",
                ),
            },
        ),
        (
            "권한",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            "중요날짜",
            {
                "fields": (
                    "last_login",
                    "date_joined",
                ),
                "classes": ("collapse",),
            },
        ),
    )

    list_display = (
        "username",
        "name",
        "email",
        "avatar",
    )
