from django.contrib.auth.models import AnonymousUser
from requests import Response
from rest_framework import viewsets,permissions,status,validators
from .serializers import CategorySerializer,IncomeSerializer,ExpenseSerializer
from .models import Category,IncomeNote,ExpenseNote

class CategoryModelViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        user = self.request.user
        print(user)
        if user is AnonymousUser:
            validators.ValidationError('eror')
        else:
            return Category.objects.filter(user_id = user)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)


class IcomeModelViewSet(viewsets.ModelViewSet):
    queryset = IncomeNote.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [permissions.AllowAny]



class ExpenseModelViewSet(viewsets.ModelViewSet):
    queryset = ExpenseNote.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.AllowAny]