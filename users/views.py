from rest_framework.views import APIView
from rest_framework.response import Response


class Me(APIView):
    def get(self, req):
        # print(f"@@@@@@@@@@@@@@@@@@@{req}")
        # print(dir(req.user))
        # user = req.user

        return Response(
            {
                "ok": "만사ok야!!",
            }
        )

요청 -> 해결 -> 응답

# 
# 함수 self req요청
