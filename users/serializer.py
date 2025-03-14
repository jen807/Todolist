from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "name",
        )


# 유저 상세 정보 -> 로그인한 유저만 볼 수 있음 username, name, password
# 유저 페이지 -> 누구든 볼 수 있음 username, name, avatar
