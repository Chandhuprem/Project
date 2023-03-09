from django.contrib import admin

# Register your models here.
from .models import MyModel
from .models import Newbook


class MyModelAdmin(admin.ModelAdmin):
    list_display=('bname','bprice','author','image')
admin.site.register(MyModel,MyModelAdmin)
class NewbookAdmin(admin.ModelAdmin):
    list_display=('images',)
admin.site.register(Newbook,NewbookAdmin)