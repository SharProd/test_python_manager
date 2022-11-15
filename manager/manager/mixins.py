from auth_user.models import User
from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework.pagination import PageNumberPagination


class DateTimeMixinModel:
    date_created = models.DateTimeField(_("date created"), auto_now_add=True, blank=True, null=True)
    date_update = models.DateTimeField(_("date update"), auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True


class NoteMixin(models.Model):
    money = models.FloatField(
        verbose_name="money",
        validators=[
            validators.MinValueValidator(0.1),
        ],
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date_created = models.DateTimeField(verbose_name="date created")
    # category =
    organization = models.CharField(max_length=80, verbose_name="organization")
    discription = models.TextField(max_length=500, verbose_name="description for payment")

    def __str__(self):
        return f"{self.money},{self.organization},{self.date_created}"

    class Meta:
        abstract = True


class CustomPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 150
