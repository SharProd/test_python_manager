from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .endpoints import CategoryModelViewSet,IncomeModelViewSet,ExpenseModelViewSet


router = DefaultRouter()
router.register('category',CategoryModelViewSet)
router.register('income',IncomeModelViewSet)
router.register('expense',ExpenseModelViewSet)


urlpatterns = [
    path("", include(router.urls)),
]