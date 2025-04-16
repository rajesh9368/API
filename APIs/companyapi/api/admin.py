from django.contrib import admin

# Register your models here.
from .models import Company,Employee
class Companyadmin(admin.ModelAdmin):
  list_display = ('name','location')
class Employeeadmin(admin.ModelAdmin):
  list_display = ('name','email')
admin.site.register(Company,Companyadmin)
admin.site.register(Employee,Employeeadmin)