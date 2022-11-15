from django.contrib.auth.models import AnonymousUser
from django.db.models import Sum
from rest_framework import response, permissions, viewsets, views

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


class UserProfilApiView(views.APIView):
    def get(self,request):
        user = self.request.user
        data = dict()
        data['expenses'] = ExpenseNote.objects.filter(user_id=user).aggregate(Sum('money'))
        data['incomes'] = IncomeNote.objects.filter(user_id=user).aggregate(Sum('money'))
        return  response.Response(data)