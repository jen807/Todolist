from django.db import models
from common.models import CommonModel


class Img(CommonModel):

    imgurl = models.URLField()

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )


# Backend <-> DATABASE

# baseURL / api / v1 / user

# res => res.DeprecationWarning
# json

# {
#     [
#         ...
#     ]
# }

# 프론트
# =>요청하여 응답받은 데이터를 이쁘게 꾸며줌

# 백엔드
# =>요청데이터를 받아서 응답해줌
