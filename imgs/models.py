from django.db import models
from common.models import CommonModel


class Img(CommonModel):

    imgurl = models.URLField()

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
