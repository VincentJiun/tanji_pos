from django.contrib import admin
from .models import Food, Foodtype, Staff, Table

# Register your models here.
admin.site.register(Food)
admin.site.register(Foodtype)
admin.site.register(Staff)
admin.site.register(Table)