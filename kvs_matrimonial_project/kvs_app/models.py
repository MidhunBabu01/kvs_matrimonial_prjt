from django.db import models

# Create your models here.
class StateCommitie(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=50,blank=False,null=False)
    phone = models.CharField(max_length=10,blank=False,null=False)
    place = models.CharField(max_length=250,blank=False,null=False)



class Taluk_choices(models.Model):
    class Meta:
        verbose_name_plural = 'Taluk choices'
    def __str__(self):
        return self.name
    name = models.CharField(max_length=50)


class Taluk(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=50,blank=False,null=False)
    phone = models.CharField(max_length=10,blank=False,null=False)
    taluk  = models.ForeignKey(Taluk_choices,on_delete=models.CASCADE,blank=False,null=False)



class Sakha(models.Model):
    def __str__(self):
        return self.sakha_no
    sakha_no = models.CharField(max_length=50,blank=False,null=False)
    taluk  = models.ForeignKey(Taluk_choices,on_delete=models.CASCADE,blank=False,null=False)