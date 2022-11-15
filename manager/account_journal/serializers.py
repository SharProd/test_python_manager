from rest_framework import serializers, request
from .models import IncomeNote,ExpenseNote,Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'




class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseNote
        fields = '__all__'
        extra_fields = {}


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeNote
        fields = '__all__'