from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Todo
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
