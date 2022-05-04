from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Client (models.Model):

    client_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True,on_delete=models.SET_NULL)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.client_name

class Project(models.Model):
    client = models.ForeignKey(Client,on_delete=models.CASCADE,related_name='Projects')
    project_name = models.CharField(max_length=100)

    def __str__(self):
        return self.client.client_name

