import datetime
from django.db import models
import django

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



class Gender_choices(models.Model):
    class Meta:
        verbose_name_plural = 'Gender'
    def __str__(self):
        return self.name
    name = models.CharField(max_length=25)



class SubCaste_choices(models.Model):
    class Meta:
        verbose_name_plural = 'Sub Caste'
    def __str__(self):
        return self.name
    name = models.CharField(max_length=25)



import re
import re
now = datetime.datetime.now()
class Matrimonial(models.Model):
    def __str__(self):
        return self.name
    created_at = models.DateField(default=django.utils.timezone.now,blank=False, null=False)
    name = models.CharField(max_length=25,blank=False,null=False)
    dob = models.DateField(blank=False,null=False)
    age = models.IntegerField(blank=True,null=True)
    phone = models.CharField(max_length=10,blank=False,null=False)
    email = models.EmailField(blank=True,null=True)
    gender = models.ForeignKey(Gender_choices,on_delete=models.CASCADE,blank=False,null=False)
    height = models.IntegerField(blank=False,null=False)
    work_place = models.CharField(max_length=25,blank=True,null=True)
    languages = models.CharField(max_length=250,blank=False,null=False)
    hobbies = models.CharField(max_length=250,blank=True,null=True)
    brother = models.IntegerField(blank=False,null=False)
    father_name = models.CharField(max_length=25,blank=False,null=False)
    father_occupation = models.CharField(max_length=25,blank=True,null=True)
    mother_name = models.CharField(max_length=25,blank=False,null=False)
    mother_occupation = models.CharField(max_length=25,blank=True,null=True)
    sister = models.IntegerField(blank=False,null=False)
    total_family_members = models.IntegerField(blank=True,null=True)
    marital_choices = (
        ('Married','Married'),
        ('Un Married','Un Married'),
        ('Divorced','Divorced'),
        ('Widow','Widow')
    )
    marital_status = models.CharField(choices=marital_choices,max_length=25,blank=False,null=False)
    subcaste = models.ForeignKey(SubCaste_choices,on_delete=models.CASCADE,blank=False,null=False)
    photo = models.ImageField(upload_to = 'pictures',blank=False,null=False)
    education_qualification = models.CharField(max_length=250,blank=False,null=False)
    occupation = models.CharField(max_length=250,blank=False,null=False)
    DISTRICT_CHOICES = (
        ('Trivandrum','Trivandrum'),
        ('Kollam','Kollam'),
        ('Pathanamthitta','Pathanamthitta'),
        ('Alappuzha','Alappuzha'),
        ('Kottayam','Kottayam'),
        ('Idukki','Idukki'),
        ('Ernakulam','Ernakulam'),
        ('Thrissur','Thrissur'),
        ('Palakkad','Palakkad'),
        ('Malappuram','Malappuram'),
        ('Kozhikode','Kozhikode'),
        ('Wayanad','Wayanad'),
        ('Kannur','Kannur'),
        ('Kasaragod','Kasaragod'),
    )
    district = models.CharField(max_length=250,choices=DISTRICT_CHOICES,blank=False,null=False)
    taluk = models.CharField(max_length=50,blank=False,null=False)
    status_choices = (
        ('Pending','Pending'),
        ('Approved','Approved')
    )
    status = models.CharField(max_length=25,choices=status_choices,default='Pending')
