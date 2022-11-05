from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id','email','last_name','first_name')
    list_filter = ('id','email','last_name')
    list_display_links = ('id','email','last_name')


admin.site.register(User,UserAdmin)

