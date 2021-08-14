from django.db import models
from django.db.models.deletion import CASCADE
from client.models import Client
from project.models import Project
# Create your models here.
class Receipt(models.Model):
    client = models.ForeignKey(to=Client,to_field='email',on_delete=CASCADE,related_name="client")
    project = models.ForeignKey(to=Project,to_field='project_name',on_delete=CASCADE,null=True,blank=True)
    date=models.DateField(null=True, blank=True)
    description=models.TextField(blank=True,null=True)
    amount=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return  f"{self.client}"