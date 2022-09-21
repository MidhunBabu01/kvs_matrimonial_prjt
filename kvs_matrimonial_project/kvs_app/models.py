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
    sakaha_name = models.CharField(max_length=50,blank=True,null=True)
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



class Star(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=25)





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
    star = models.ForeignKey(Star,on_delete=models.CASCADE,blank=False,null=False)
    height = models.IntegerField(blank=False,null=False)
    work_place = models.CharField(max_length=25,blank=True,null=True)
    languages = models.CharField(max_length=250,blank=True,null=True)
    hobbies = models.CharField(max_length=250,blank=True,null=True)
    brother = models.IntegerField(blank=False,null=False)
    father_name = models.CharField(max_length=25,blank=False,null=False)
    father_occupation = models.CharField(max_length=25,blank=False,null=False)
    mother_name = models.CharField(max_length=25,blank=False,null=False)
    mother_occupation = models.CharField(max_length=25,blank=False,null=False)
    sister = models.IntegerField(blank=False,null=False)
    total_family_members = models.IntegerField(blank=False,null=False)
    marital_choices = (
        ('Un Married','Un Married'),
        ('Second Marriage','Second Marriage'),
        ('Divorced','Divorced'),
        ('Widow','Widow')
    )
    marital_status = models.CharField(choices=marital_choices,max_length=25,blank=False,null=False)
    subcaste = models.ForeignKey(SubCaste_choices,on_delete=models.CASCADE,blank=True,null=True)
    photo = models.ImageField(upload_to = 'pictures',blank=True,null=True)
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
    gaurdian_name = models.CharField(max_length=50,blank=False,null=False)
    # gaurdian_mobile = models.CharField(max_length=10,blank=True,null=True)
    status_choices = (
        ('Pending','Pending'),
        ('Approved','Approved')
    )
    status = models.CharField(max_length=25,choices=status_choices,default='Pending')
