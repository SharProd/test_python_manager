from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .endpoints import (
    CategoryModelViewSet,
    ExpenseModelViewSet,
    IncomeModelViewSet,
    UserProfileApiView,
)

router = DefaultRouter()
router.register("category", CategoryModelViewSet)
router.register("income", IncomeModelViewSet)
router.register("expense", ExpenseModelViewSet)


urlpatterns = [path("", include(router.urls)), path("user_profile/", UserProfileApiView.as_view(), name="user_profile")]
