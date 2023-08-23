import datetime
from unicodedata import category
from django.db import models
import django
from django.contrib.auth.models import User

# Create your models here.

class ExtendedUserModel(models.Model):
    class Meta:
        verbose_name_plural = 'Extended User Model'
    def __str__(self):
        return self.user.username
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    district = models.CharField(max_length=50)





class StateCommitie(models.Model):
    class Meta:
        verbose_name_plural = 'State Commitie'
    def __str__(self):
        return self.name
    name = models.CharField(max_length=50,blank=False,null=False)
    phone = models.CharField(max_length=10,blank=False,null=False)
    place = models.CharField(max_length=250,blank=False,null=False)
    photo = models.ImageField(upload_to='state commitie', blank=True,null=True)



class Taluk_choices(models.Model):
    class Meta:
        verbose_name_plural = 'Add Union'
    def __str__(self):
        return self.name
    name = models.CharField(max_length=50)


class Taluk(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=50,blank=False,null=False)
    phone = models.CharField(max_length=10,blank=False,null=False)
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
    district = models.CharField(max_length=50,choices=DISTRICT_CHOICES)
    taluk  = models.ForeignKey(Taluk_choices,on_delete=models.CASCADE,blank=False,null=False)



class Sakha(models.Model):
    def __str__(self):
        return self.sakha_no
    sakha_no = models.CharField(max_length=50,blank=False,null=False)
    sakaha_name = models.CharField(max_length=50,blank=True,null=True)
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
    district = models.CharField(max_length=50,choices=DISTRICT_CHOICES)
    taluk  = models.ForeignKey(Taluk_choices,on_delete=models.CASCADE,blank=False,null=False)



class Gender_choices(models.Model):
    class Meta:
        verbose_name_plural = 'Add Gender'
    def __str__(self):
        return self.name
    name = models.CharField(max_length=25)



class SubCaste_choices(models.Model):
    class Meta:
        verbose_name_plural = 'Add Subcaste'
    def __str__(self):
        return self.name
    name = models.CharField(max_length=25)



class Star(models.Model):
    class Meta:
        verbose_name_plural = 'Add Star'
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
    status = models.CharField(max_length=25,choices=status_choices,default='Approved')





class Insurence_category(models.Model):
    class Meta:
        verbose_name_plural = 'Add Insurence category'
    def __str__(self):
        return self.name
    name = models.CharField(max_length=50)
    

class Id_details_choices(models.Model):
    class Meta:
        verbose_name_plural = 'Add Id card choices'
    def __str__(self):
        return self.name
    name = models.CharField(max_length=50)


class Payment_details_choices(models.Model):
    class Meta:
        verbose_name_plural = 'Add Payment Details choices'
    def __str__(self):
        return self.name
    name = models.CharField(max_length=50)




class Services(models.Model):
    class Meta:
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.name
    category = models.ForeignKey(Insurence_category,on_delete=models.CASCADE,blank=False,null=False)
    name = models.CharField(max_length=25,blank=False,null=False)
    mobile_no = models.CharField(max_length=10,blank=False,null=False)
    joining_date = models.DateField(blank=True,null=True)
    id_details = models.ForeignKey(Id_details_choices,on_delete=models.CASCADE,blank=False,null=False)
    id_no = models.CharField(max_length=25,blank=False,null=False)
    sakha_no = models.CharField(max_length=25,blank=False,null=False)
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
    district = models.CharField(max_length=50,choices=DISTRICT_CHOICES)
    taluk = models.CharField(max_length=25,blank=False,null=False)
    payment_details = models.ForeignKey(Payment_details_choices,on_delete=models.CASCADE,blank=False,null=False)
    proposed_by_name = models.CharField(max_length=25,blank=True,null=True)
    proposed_by_contact_no = models.CharField(max_length=25,blank=True,null=True)
    STATUS_CHOISES = (
        ('Pending','Pending'),
        ('Approved','Approved')
    )
    status = models.CharField(max_length=25,choices=STATUS_CHOISES,default='Pending')

class Sex_Choices(models.Model):
    class Meta:
        verbose_name_plural = 'Add Sex'
    name = models.CharField(max_length=10,blank=True,null=True)
    def __str__(self):
        return self.name

class Join_Kvs(models.Model):
    class Meta:
        verbose_name_plural = 'Join Kvs'
    added_by = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=25,blank=False,null=False)
    sex = models.ForeignKey(Sex_Choices,on_delete=models.CASCADE,blank=True,null=True)
    age = models.IntegerField(blank=True,null=True)
    dob = models.DateField(blank=True,null=True)
    mobile = models.CharField(max_length=10,blank=False,null=False)
    address = models.TextField(blank=False,null=False)
    place = models.CharField(max_length=25,blank=False,null=False)
    # taluk = models.CharField(max_length=25,blank=False,null=False)
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
    district = models.CharField(max_length=50,choices=DISTRICT_CHOICES,blank=True,null=True)
    union = models.ForeignKey(Taluk_choices,on_delete=models.CASCADE,blank=True,null=True)
    sakha_no = models.CharField(max_length=25,blank=True,null=True)
    id_proof = models.ForeignKey(Id_details_choices,on_delete=models.CASCADE,blank=False,null=False)
    id_proof_no = models.CharField(max_length=25,blank=True,null=True)
    payment_details = models.ForeignKey(Payment_details_choices,on_delete=models.CASCADE,blank=True,null=True)
    STATUS_CHOISES = (
        ('Pending','Pending'),
        ('Approved','Approved')
    )
    membership_no = models.CharField(max_length=50,blank=True,null=True)
    status = models.CharField(max_length=25,choices=STATUS_CHOISES,default='Pending')




class Databank(models.Model):
    def __str__(self):
        return self.name
    category = models.CharField(max_length=50,blank=False,null=False)
    name = models.CharField(max_length=50,blank=False,null=False)
    mobile = models.CharField(max_length=10,blank=False,null=False)
    photo = models.ImageField(upload_to='databankpic',blank=True,null=True)
    occupation = models.CharField(max_length=50,blank=False,null=False)
    district = models.CharField(max_length=50,blank=False,null=False)
    taluk = models.CharField(max_length=50,blank=False,null=False)
    workplace = models.CharField(max_length=50,blank=False,null=False)
    contact_person = models.CharField(max_length=50,blank=False,null=False)
    status_choices = (
        ('Hide','Hide'),
        ('Unhide','Unhide')
    )
    status = models.CharField(max_length=25,choices=status_choices,default='Unhide')
    
