from django.db import models

# Create your models here.
class StateCommitie(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=50,blank=False,null=False)
    phone = models.CharField(max_length=10,blank=False,null=False)
    place = models.CharField(max_length=250,blank=False,null=False)

