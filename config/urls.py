"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # =>경로를 수정하면 그게 적용이 됨 장고에서 경로에 해당하는 곳은 여기서 지정할 수 있다.
    path("api/v1/users/", include("users.urls")),
    path("api/v1/todos/", include("todos.urls")),
]

# todo 컨텐츠들
# todo 상세 페이지 -> 수정, 삭제
# todo 생성
