from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Todo
from rest_framework import status
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import IsAuthenticated
from .serializer import TodoSerializer


class Todos(APIView):
    permission_classes = [IsAuthenticated]
    # =>로그인 시에만 볼 수 있음 (권한이 있어야 가능하게 만들어준다)

    def get(self, req):
        # todos = Todo.objects.all()
        todos = Todo.objects.filter(user=req.user)

        serializer = TodoSerializer(
            todos,
            many=True,
        )
        # print(f"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@{todos}")

        return Response(serializer.data)

    def post(self, req):
        serializer = TodoSerializer(data=req.data)

        if serializer.is_valid():
            todo = serializer.save(user=req.user)
            serializer = TodoSerializer(todo)
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

        # 1. 등록하면 -> 유저가 작성한 내용을 가져와야함 req.data
        # 2. 가져온 유저의 데이터 json을 -> python코드로 변환 과정이 필요함 ->serializer
        # 3. 유효성 검사 ok (isvald) -> 저장
        # 4. 파이썬 코드를 -> json으로 변환 -> serializer (serializer,return은세트)


class TodoDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            raise NotFound

    def get(self, req, pk):
        # print(pk)
        todo = self.get_object(pk)

        if todo.user != req.user:
            raise PermissionDenied

        serializer = TodoSerializer(todo)

        return Response(serializer.data)

    def put(self, req, pk):
        todo = self.get_object(pk)

        serializer = TodoSerializer(
            todo,
            data=req.data,
            partial=True,
        )

        if serializer.is_valid():
            todo = serializer.save(user=req.user)
            serializer = TodoSerializer(todo)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, req, pk):
        todo = self.get_object(pk)

        if todo.user != req.user:
            raise PermissionDenied

        todo.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
