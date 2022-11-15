from rest_framework import generics, permissions, viewsets
from manager.mixins import CustomPagination
from .models import User
from .serializers import RegistrationSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = CustomPagination


class RegisterViewApi(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.AllowAny]


