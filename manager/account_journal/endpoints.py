from rest_framework import viewsets,permissions
from .serializers import CategorySerializer,IncomeSerializer,ExpenseSerializer
from .models import Category,IncomeNote,ExpenseNote


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]


class IcomeModelViewSet(viewsets.ModelViewSet):
    queryset = IncomeNote.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [permissions.AllowAny]



class ExpenseModelViewSet(viewsets.ModelViewSet):
    queryset = ExpenseNote.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.AllowAny]