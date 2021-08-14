from django.db import models

# Create your models here.
class Client(models.Model):
    support_list = [
        ('Yes','Yes'),
        ('No','No'),
    ]
    name=models.CharField(max_length = 500, unique=True)
    phone_number1=models.CharField(max_length = 10, unique=True)
    phone_number2=models.CharField(max_length = 10, unique=True)
    email = models.CharField(max_length = 150, unique=True)
    aggrement_start_date=models.DateField(null=True, blank=True)
    aggrement_end_date=models.DateField(null=True, blank=True)
    supporting = models.CharField(max_length = 50,choices = support_list,default ='Yes',blank=True,null=True)

    def __str__(self):
        return  f"{self.name}"
