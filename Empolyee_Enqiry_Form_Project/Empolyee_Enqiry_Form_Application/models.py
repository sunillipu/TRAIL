from django.db import models
from django.db import models



class Employee_Enquiry_Data(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mobile_no = models.BigIntegerField()
    qualification = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    skill = models.CharField(max_length=50)
    def __str__(self):
        return self.first_name



