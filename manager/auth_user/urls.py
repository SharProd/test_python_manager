from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .endpoints import UserViewSet,RegisterViewApi


router = DefaultRouter()
router.register('user_list',UserViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("register/", RegisterViewApi.as_view(), name="create_user"),

]