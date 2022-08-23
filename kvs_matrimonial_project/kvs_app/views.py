from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User,auth
from .forms import StateCommiteForm
from .models import StateCommitie
# Create your views here.
def index(request):
    return render(request,'index.html')


def executiveforum(request):
    state_commite = StateCommitie.objects.all()
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
    return render(request,'taluk.html')

def sakha(request):
    return render(request,'sakha.html')


def matrimonial_service(request):
    return render (request,'materimonialservices.html')


def profile_details(request):
    return render(request,'viewprofile.html')


def marrige_register(request):
    return render(request,'marriageregister.html')


def contact(request):
    return render(request,'contact.html')





def logout(request):
    auth.logout(request)
    return redirect('kvs_app:index')