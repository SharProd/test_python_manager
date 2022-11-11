from django.contrib import admin
from .models import IncomeNote,ExpenseNote,Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title','user')
    list_filter = ('id','title','user')
    list_display_links = ('id','title','user')

class IncomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'money', 'organization', 'date_created')
    list_filter = ('id', 'money', 'date_created')
    list_display_links = ('id', 'money', 'date_created')


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'money', 'organization', 'date_created')
    list_filter = ('id', 'money', 'date_created')
    list_display_links = ('id', 'money', 'date_created')


admin.site.register(IncomeNote, IncomeAdmin)
admin.site.register(ExpenseNote, ExpenseAdmin)
admin.site.register(Category,CategoryAdmin)