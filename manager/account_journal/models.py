from django.db import models
from manager.mixins import NoteMixin

class Category(models.Model):
    title = models.CharField(max_length=50,verbose_name='payment category')

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
