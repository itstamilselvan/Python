from django.contrib import admin
from .models import product,orders
from django.contrib.auth.models import Group

# Register your models here.

class productadmin(admin.ModelAdmin):
    list_display = ('name','quantity','category')
    list_filter = ['category']
    
admin.site.site_header = 'KENINVENTORY DASHBOARD'

admin.site.register(product,productadmin)
admin.site.register(orders)

# admin.site.unregister(Group)