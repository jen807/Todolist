from django.contrib import admin
from .models import Img

# Register your models here.


@admin.register(Img)
class ImgAdmin(admin.ModelAdmin):
    list_display = (
        "imgurl",
        "user",
    )
