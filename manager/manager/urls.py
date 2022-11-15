from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api_auth/", include("auth_user.urls"), name="api_user"),
    path("api_journal/", include("account_journal.urls"), name="api_journal"),
    path("api_auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api_auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
