from django.db import models
from manager.mixins import NoteMixin
from auth_user.models import User


class Category(models.Model):
    title = models.CharField(max_length=50,verbose_name='payment category')
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'payment category'
        verbose_name_plural = 'payment categories'


class IncomeNote(NoteMixin):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'income note'
        verbose_name_plural = 'income notes'


class ExpenseNote(NoteMixin):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'expense note'
        verbose_name_plural = 'expense notes'
