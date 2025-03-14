from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ParseError
from .serializer import UserSerializer
from rest_framework import status


class Me(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, req):
        # print(f"@@@@@@@@@@@@@@@@@@@{req}")
        # print(dir(req.user))
        user = req.user

        serializer = UserSerializer(user)

        return Response(serializer.data)

    def put(self, req):
        user = req.user
        serializer = UserSerializer(
            user,
            data=req.data,
            partial=True,
        )

        if serializer.is_valid():
            user = serializer.save()
            # 시리얼라이즈 해줘
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Signup(APIView):
    def post(self, req):
        username = req.data.get("username")
        password = req.data.get("password")

        if not username or not password:
            raise ParseError("아이디 및 패스워드는 필수 입니다.")

        # 유저가 입력한 데이터 가지고 와서 유효성 검사 후
        # 데이터베이스에 유저 정보를 저장한 뒤
        # 응답을 회원가입 되었습니다... 라고 뜨게

        # 패스워드를 -> 해시로
        try:
            validate_password(password)
            # =>해시화 안하고 그냥 패스워드 유효검사
        except Exception as e:
            raise ParseError(e)

        serialzer = UserSerializer(data=req.data)

        if serialzer.is_valid():
            user = serialzer.save()
            user.set_password(password)
            # password hash
            user.save()
            serializer = UserSerializer(user)
            return Response({"ok": "화원가입 되었습니다."})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # serializer 쓰면 그냥 serializer


class Login(APIView):
    def post(self, req):
        username = req.data.get("username")
        password = req.data.get("password")

        if not username and not password:
            raise ParseError("아이디나 비밀번호를 입력해주세요")

        user = authenticate(
            req,
            username=username,
            password=password,
        )

        if user:
            login(req, user)
            return Response(
                {"ok": "로그인 되었습니다."},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"error": "로그인에 실패 하였습니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )


class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, req):
        logout(req)
        return Response(
            {"ok": "로그아웃 되었습니다."},
            status=status.HTTP_200_OK,
        )


class ChangePassword(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, req):
        user = req.user
        current_password = req.data.get("current_password")
        new_password = req.data.get("new_password")

        if not current_password or not new_password:
            raise ParseError("빈값 안돼요🙅‍♀️")

        if user.check_password(current_password):
            user.set_password(new_password)
            user.save()
            return Response(
                {"ok": "패스워드 변경완료"},
                status=status.HTTP_200_OK,
            )
        else:
            raise ParseError("패스워드 확인해주세요")


# class EditUser(APIView):
#     permission_classes = [IsAuthenticated]

#     def put(self, req):
#         current_name = req.data.get("current_name")
#         new_name = req.data.get("new_name")

#         current_email = req.data.get("current_email")
#         new_email = req.data.get("new_email")


# raise 강제 발생
# return 그저 반환.

# 유저가 입력한 정보를 가지고 와서
# 빈값인지 아닌지 유효성 검사하고
# 새로운 비밀번호를 해시처리하여 새로운 패스워드를 저장하고
# 비밀번호가 변경되었다고 응답해야 됨
# 그리고 문제가 발생하면 예외처리


# {
# "current_password":"123ppppp",
# "new_password":"123123ppppp"
# }

# {
# "username":"test12",
# "password":"123123ppppp",
# "name":"hello"
# }


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
