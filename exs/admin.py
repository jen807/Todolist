from django.contrib import admin
from .models import Exs


# Register your models here.
@admin.register(Exs)
class ExsAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "user",
    )
