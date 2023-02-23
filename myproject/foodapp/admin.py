from django.contrib import admin
from .models import Food

# Register your models here.
class FoodAdmin(admin.ModelAdmin):
    list_display = ['fname', 'fdesc', 'fprice', 'fimg']

admin.site.register(Food, FoodAdmin)