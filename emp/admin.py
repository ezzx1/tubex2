from django.contrib import admin
from . import models
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
# Register your models here.
admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(models.department)
class SuppAdmin(admin.ModelAdmin):
    list_display=('الاسم','رقم_التواصل','العنوان')
admin.site.register(models.suppliers,SuppAdmin)
admin.site.site_header="TUBEX"
admin.site.site_title="TUBEX"

class EmpAdmin(admin.ModelAdmin):
    
    list_display=('الاسم','المرتب','القطاع')
    list_filter=('القطاع',)
    search_fields=('الاسم',)
    

admin.site.register(models.emp,EmpAdmin)
