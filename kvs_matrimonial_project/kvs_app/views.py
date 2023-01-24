import datetime
from unittest import result
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User,auth
from .forms import MatrimonialUpdateForm, StateCommiteForm,TalukForm,SakhaForm,MatrimonialForm,MatrimonialUpdateForm,Services_Add_Form,Services_Admin_Edit_Form,Join_Kvs_Add_Form,Join_Kvs_Admin_Update
from .models import Join_Kvs, Matrimonial, Sakha, Services, StateCommitie,Taluk
import re
now = datetime.datetime.now()
from django.http.response import JsonResponse
from django.db.models import Q

# MAIL SENDING SECTION
from django.core.mail import  EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')


def executiveforum(request):
    state_commite = StateCommitie.objects.all().order_by('-id')
    if request.method == 'POST':
        form = StateCommiteForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('kvs_app:executiveforum')
    else:
        form = StateCommiteForm()
    return render(request,'executiveforum.html',{'form':form,'state_commite':state_commite})


def executiveforum_update(request,update_id):
    update = StateCommitie.objects.filter(id=update_id).first()
    if request.method == 'POST':
        form = StateCommiteForm(request.POST,request.FILES,instance=update)
        if form.is_valid():
            form.save()
            return redirect('kvs_app:executiveforum')
    else:
        update = StateCommitie.objects.filter(id=update_id).first()
        form = StateCommiteForm(instance=update)
    return render(request,'executiveforumreg.html',{'form':form})


def executiveforum_delete(request,dlt_id):
    dlt = StateCommitie.objects.filter(id=dlt_id)
    dlt.delete()
    return redirect('kvs_app:executiveforum')





def taluk(request):
    taluk = Taluk.objects.all().order_by('-id')
    if request.method == 'POST':
        form = TalukForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kvs_app:taluk')
    else:
        form = TalukForm()
    return render(request,'taluk.html',{'form':form,'taluk':taluk})


def taluk_update(request,taluk_id):
    update  = Taluk.objects.filter(id=taluk_id).first()
    if request.method == 'POST':
        form = TalukForm(request.POST,instance=update)
        if form.is_valid():
            form.save()
            return redirect('kvs_app:taluk')
    else:
        update  = Taluk.objects.filter(id=taluk_id).first()
        form = TalukForm(instance=update)
    return render(request,'talukreg.html',{'form':form})



def taluk_delete(request,taluk_id):
    taluk = Taluk.objects.filter(id=taluk_id)
    taluk.delete()
    return redirect('kvs_app:taluk')



def sakha(request):
    sakha = Sakha.objects.all().order_by('-id')
    if request.method == 'POST':
        form = SakhaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kvs_app:sakha')
    else:
        form = SakhaForm()
    return render(request,'sakha.html',{'form':form,'sakha':sakha})


def sakha_update(request,sakha_id):
    update  = Sakha.objects.filter(id=sakha_id).first()
    if request.method == 'POST':
        form = SakhaForm(request.POST,instance=update)
        if form.is_valid():
            form.save()
            return redirect('kvs_app:sakha')
    else:
        update  = Sakha.objects.filter(id=sakha_id).first()
        form = SakhaForm(instance=update)
    return render(request,'sakhareg.html',{'form':form})




def sakha_delete(request,sakha_id):
    sakha = Sakha.objects.filter(id=sakha_id)
    sakha.delete()
    return redirect('kvs_app:sakha')



def bride(request):
    bride = Matrimonial.objects.filter(gender__name='Bride',status='Approved').order_by('-id')
    return render(request,'materimonialservices.html',{'result':bride})

def grooms(request):
    grooms = Matrimonial.objects.filter(gender__name='Groom',status='Approved').order_by('-id')
    return render (request,'materimonialservices-grooms.html',{'result':grooms})

def pending(request):
    pending = Matrimonial.objects.filter(status='Pending').order_by('-id')
    return render(request,'materimonialservices-pending.html',{'result':pending})


def matrimonial_update(request,update_id):
    if request.method == 'POST':
        update = Matrimonial.objects.filter(id=update_id).first()
        form = MatrimonialUpdateForm(request.POST,request.FILES,instance=update)
        if form.is_valid():
            form.save()
            messages.success(request,'Succesfully Updated')
            return redirect('kvs_app:index')
    else:
        update = Matrimonial.objects.filter(id=update_id).first()
        form = MatrimonialUpdateForm(instance=update)
    return render(request,'matrimony-update.html',{'form':form})


def matrimony_bride_search(request):
    Query = None
    result = None
    if 'q' in request.GET:
        Query = request.GET.get('q')
        result = Matrimonial.objects.filter(Q(name__icontains=Query),gender__name='Bride')
    return render(request,'bride-search-result.html',{'result':result})


def matrimony_grooms_search(request):
    Query = None
    result = None
    if 'q' in request.GET:
        Query = request.GET.get('q')
        result = Matrimonial.objects.filter(Q(name__icontains=Query),gender__name='Groom')
    return render(request,'grooms-search-result.html',{'result':result})



def profile_details(request,details_id):
    details = Matrimonial.objects.filter(id=details_id)
    return render(request,'viewprofile.html',{'details':details})




def matrimoni_delete(request,dlt_id):
    dlt = Matrimonial.objects.filter(id=dlt_id)
    dlt.delete()
    return redirect('kvs_app:bride')


def marrige_register(request):
    if request.method == 'POST':
        form = MatrimonialForm(request.POST,request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            year = form.cleaned_data['dob']
            year = re.split(r'-',str(year))[0]
            age = int(now.year)-int(year)
            data.age = age
            data.save()
            print('UPDATED')
            messages.success(request,'Please wait for the Admin approval')
            return redirect('kvs_app:marrige_register')
    else:
        form = MatrimonialForm()
        print('NOT UPDATED')
    return render(request,'marriageregister.html',{'form':form})




def health_insurance(request):
    result = Services.objects.filter(category__name='Health Insurance',status='Approved').order_by('-id')
    if request.method == 'POST':
        form = Services_Add_Form(request.POST)
        if form.is_valid():
            form.save()
            print('success')
            messages.success(request,'Wait for the Admin Approval')
            return redirect('kvs_app:index')
    else:
        form = Services_Add_Form()
    return render(request,'health-insurance.html',{'form':form,'result':result})



# def health_insurance_update(request,update_id):
#     update = Services.objects.filter(id=update_id).first()
#     if request.method == 'POST':
#         form = Services_Add_Form(request.POST,instance=update)
#         if form.is_valid():
#             form.save()
#             return redirect('kvs_app:index')
#     else:
#         form = Services_Add_Form(instance=update)
#     return render(request,'insurance-update.html',{'form':form})


def insurance_delete(request,dlt_id):
    dlt = Services.objects.filter(id=dlt_id)
    dlt.delete()
    messages.success(request,'Succesfully Deleted')
    return redirect('kvs_app:index')



def accident_insurance(request):
    result = Services.objects.filter(category__name='Accident Insurance',status='Approved').order_by('-id')
    if request.method == 'POST':
        form = Services_Add_Form(request.POST)
        if form.is_valid():
            form.save()
            print('success')
            messages.success(request,'Wait for the Admin Approval')
            return redirect('kvs_app:index')
    else:
        form = Services_Add_Form()
    return render(request,'accident-insurance.html',{'form':form,'result':result})




def insurance_pending(request):
    pending = Services.objects.filter(status='Pending').order_by('-id')
    return render(request,'insurance-pending.html',{'pending':pending})


def insurance_update(request,update_id):
    update = Services.objects.filter(id=update_id).first()
    if request.method == 'POST':
        form = Services_Admin_Edit_Form(request.POST,instance=update)
        if form.is_valid():
            form.save()
            messages.success(request,'Succesfully Updated')
            return redirect('kvs_app:index')
    else:
        form = Services_Admin_Edit_Form(instance=update)
    return render(request,'pending-insurance-update.html',{'form':form})



def join_kvs(request):
    membership_list = Join_Kvs.objects.filter(status='Approved').order_by('-id')
    if request.method == 'POST':
        form = Join_Kvs_Add_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Membership will be Approved only after verification of Admin')
            return redirect('kvs_app:join_kvs')
    else:
        form = Join_Kvs_Add_Form()
    return render(request,'join-kvs.html',{'form':form,'membership_list':membership_list})



def join_kvs_update(request,update_id):
    update = Join_Kvs.objects.filter(id=update_id).first()
    if request.method == 'POST':
        form = Join_Kvs_Admin_Update(request.POST,instance=update)
        if form.is_valid():
            form.save()
            messages.success(request,'Succesfully Updated')
            return redirect('kvs_app:join_kvs')
    else:
        form = Join_Kvs_Admin_Update(instance=update)
    return render(request,'join-kvs-update.html',{'form':form})




def join_kvs_pending(request):
    pending = Join_Kvs.objects.filter(status = 'Pending').order_by('-id')
    return render(request,'join-kvs-pending.html',{'pending':pending})



def join_kvs_delete(request,dlt_id):
    dlt = Join_Kvs.objects.filter(id=dlt_id)
    dlt.delete()
    messages.success(request,'Succesfully Deleted')
    return redirect('kvs_app:join_kvs')





def contact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        emaill = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('sub1')
        message = request.POST.get('message')
        template = render_to_string('email.html',{'name':name,'phone':phone,'subject':subject,'message':message,'emaill':emaill})
        email = EmailMessage(
            'Kerala Viswakarma Sabha', #subject
            template, #body
            emaill, #sender mail id
            ['artisankendram@gmail.com'] #recever mail id
        )
        email.fail_silently = False
        email.send()
        messages.success(request,'Email send succesfully')
        print('Email Send')
        return redirect('kvs_app:contact')
    return render(request,'contact.html')



# ACCOUNT SECTION

def login(request):
    if 'username' in request.session:
        return redirect("kvs_app:index")
    elif request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password) 
        if user is not None:
            request.session['username'] = username
            auth.login(request,user)
            return JsonResponse(
                {'success':True},
                safe=False
            )
        else:
            auth.login
            return JsonResponse(
                {'success':False},
                safe=False
            )
    else:
        return render(request,'login.html')



def logout(request):
    auth.logout(request)
    return redirect('kvs_app:index')