from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializer import UserSerializer


class Me(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, req):
        # print(f"@@@@@@@@@@@@@@@@@@@{req}")
        # print(dir(req.user))
        user = req.user

        serializer = UserSerializer(user)

        return Response(serializer.data)


# serializer = 번역기
# 코드를 작성하면 컴퓨터가 코드를 모른다
# 우리가 작성한 코드를 컴퓨터가 이해되게 변경하는 걸 컴파일 ->2진법
# python code -> json으로 응답
# 브라우저가 python 코드를 알까?
# serializer를 통해 json 형식으로 변환
# serializer -> django기본적으로 가지고 있으나, 구렷음
# 요청 -> 해결 -> 응답

#
# 함수 self req요청
