from django.db import models
from django.utils import timezone

# Create your models here.
class Placey(models.Model):
    name = models.TextField(blank=True,null=True,default='')
    longitude = models.CharField(max_length=20,blank=True,null=True,default='')
    latitude = models.CharField(max_length=20,blank=True,null=True,default='')
    category = models.CharField(max_length=2,blank=True,null=True,default=0)

    def publish(self):
        self.joined_on = timezone.now()
        self.save()

    def __str__(self):
        return self.name