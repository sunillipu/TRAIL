from django.contrib import admin
from .models import Employee_Enquiry_Data

class EmployeeData(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','mobile_no','qualification','location','skill']


admin.site.register(Employee_Enquiry_Data,EmployeeData)


# Register your models here.
