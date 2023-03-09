from django.contrib import admin

# Register your models here.
from .models import Store


class StoreAdmin(admin.ModelAdmin):
    list_display=('username','email','phone','bookname','Authorname')
admin.site.register(Store,StoreAdmin)
