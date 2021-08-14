from django.db import models
from django.db.models.deletion import CASCADE
from client.models import Client
from django.contrib.auth.models import User
# Create your models here.
class Project(models.Model):
    status_list = [
        ('Lead','Lead'),
        ('Confirmed','Confirmed'),
        ('Requirement Gathering','Requirement Gathering'),
        ('In Progress','In Progress'),
        ('On Hold','On Hold'),
        ('Client side hold','Client side hold'),
        ('Complete','Complete'),
        ('Deployed','Deployed'),
    ]

    type_list = [
        ('Website','Website'),
        ('Application','Application'),
        ('Digital Marketing','Digital Marketing'),
    ]

    support_list = [
        ('Yes','Yes'),
        ('No','No'),
    ]

    project_name=models.CharField(max_length = 500, unique=True)
    client = models.ForeignKey(to=Client,to_field='email',on_delete=CASCADE)
    assigned_to=models.ForeignKey(to=User,null=True,blank=True,on_delete=models.PROTECT) 
    status = models.CharField(max_length = 50,choices = status_list,default ='Lead',blank=True,null=True)
    status_description=models.TextField(blank=True,null=True)
    type = models.CharField(max_length = 50,choices = type_list,default ='Website',blank=True,null=True)
    project_start_date=models.DateField(null=True, blank=True)
    project_end_date=models.DateField(null=True, blank=True)
    domain_detail = models.TextField(blank=True,null=True)
    hosting_detail = models.TextField(blank=True,null=True)
    domain_expiry_date=models.DateField(null=True, blank=True)
    hosting_expiry_date=models.DateField(null=True, blank=True)
    credentials = models.TextField(blank=True,null=True)
    supporting = models.CharField(max_length = 50,choices = support_list,default ='Yes',blank=True,null=True)
    
    def __str__(self):
        return  f"{self.project_name}"
