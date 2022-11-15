from django.contrib.auth.models import AnonymousUser
from rest_framework import permissions, viewsets

from .models import Category, ExpenseNote, IncomeNote
from .serializers import CategorySerializer, ExpenseSerializer, IncomeSerializer


class CategoryModelViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user is AnonymousUser:
            pass
        else:
            return Category.objects.filter(user_id=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class IncomeModelViewSet(viewsets.ModelViewSet):
    queryset = IncomeNote.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user is AnonymousUser:
            pass
        else:
            return IncomeNote.objects.filter(user_id=user)

    def perform_create(self, serializer):
        user = self.request.user
        category_list = list(Category.objects.filter(user_id=user).values("id"))
        id_category_list = tuple(map(lambda x: x["id"], category_list))
        request_category = self.request.data["category"]
        if int(request_category) in id_category_list:
            serializer.save(user=self.request.user)


class ExpenseModelViewSet(viewsets.ModelViewSet):
    queryset = ExpenseNote.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user is AnonymousUser:
            pass
        else:
            return ExpenseNote.objects.filter(user_id=user)

    def perform_create(self, serializer):
        user = self.request.user
        category_list = list(Category.objects.filter(user_id=user).values("id"))
        id_category_list = tuple(map(lambda x: x["id"], category_list))
        request_category = self.request.data["category"]
        if int(request_category) in id_category_list:
            serializer.save(user=self.request.user)
