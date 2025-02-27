from django.db import models
from common.models import CommonModel

# Create your models here.


class Todo(CommonModel):
    title = models.CharField(
        max_length=100,
    )

    payload = models.TextField()

    date = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        # 유저를 삭제하면 todo도 삭제함
    )

    def __str__(self):
        return self.title

    # class Meta:
    class Meta:
        verbose_name_plural = "할일"
