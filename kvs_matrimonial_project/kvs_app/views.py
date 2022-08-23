from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User,auth
from .forms import StateCommiteForm,TalukForm,SakhaForm
from .models import Sakha, StateCommitie,Taluk
# Create your views here.
def index(request):
    return render(request,'index.html')


def executiveforum(request):
    state_commite = StateCommitie.objects.all().order_by('-id')
    if request.method == 'POST':
        form = StateCommiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kvs_app:executiveforum')
    else:
        form = StateCommiteForm()
    return render(request,'executiveforum.html',{'form':form,'state_commite':state_commite})


def executiveforum_update(request,update_id):
    update = StateCommitie.objects.filter(id=update_id).first()
    if request.method == 'POST':
        form = StateCommiteForm(request.POST,instance=update)
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
    sakha = Sakha.objects.all()
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


def matrimonial_service(request):
    return render (request,'materimonialservices.html')


def profile_details(request):
    return render(request,'viewprofile.html')


def marrige_register(request):
    return render(request,'marriageregister.html')

from django.core.mail import  EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect

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
            ['midhunkb57@gmail.com'] #recever mail id
        )
        email.fail_silently = False
        email.send()
        print('Email Send')
        return redirect('kvs_app:contact')
    return render(request,'contact.html')





def logout(request):
    auth.logout(request)
    return redirect('kvs_app:index')