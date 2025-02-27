from django.db import models
from common.models import CommonModel

# Create your models here.


class Exs(CommonModel):
    title = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
