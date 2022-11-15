from rest_framework import serializers

from .models import Category, ExpenseNote, IncomeNote


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseNote
        fields = "__all__"
        extra_fields = {}


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeNote
        fields = "__all__"


# class UserProfileSerializer(serializers.Serializer):
#     user = UserSerializer(required=True)
#     expenses = serializers.FloatField()
#     all_expenses = serializers.FloatField()
#     incomes = serializers.FloatField()
#     all_incomes = serializers.FloatField()
