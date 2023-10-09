import datetime
from unittest import result
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User,auth
from .forms import DatabankEditForm, MatrimonialUpdateForm, StateCommiteForm,TalukForm,SakhaForm,DatabankAddForm,MatrimonialUpdateForm,Services_Add_Form,Services_Admin_Edit_Form,Join_Kvs_Add_Form,Join_Kvs_Admin_Update
from .models import Databank, ExtendedUserModel, Join_Kvs, Matrimonial, Sakha, Services, StateCommitie,Taluk
import re
now = datetime.datetime.now()
from django.http.response import JsonResponse
from django.db.models import Q
from django.contrib import messages
# MAIL SENDING SECTION
from django.core.mail import  EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.contrib import messages
import xlwt

# Create your views here.
def index(request):
    return render(request,'index.html')


def executiveforum(request):
    if request.method == 'POST':
        form = StateCommiteForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('kvs_app:executiveforum')
    else:
        form = StateCommiteForm()
    state_commite = StateCommitie.objects.all().order_by('-id')
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
    
    if request.method == 'POST':
        form = TalukForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kvs_app:taluk')
    else:
        form = TalukForm()
    if request.user.is_superuser:
        taluk = Taluk.objects.all().order_by('-id')
        return render(request,'taluk.html',{'form':form,'taluk':taluk})
    elif request.user.is_staff:
        district = request.user.extendedusermodel.district
        taluk = Taluk.objects.filter(district=district).order_by('-id')
        return render(request,'taluk.html',{'form':form,'taluk':taluk})
    else:
        taluk = Taluk.objects.all().order_by('-id')
        return render(request,'taluk.html',{'form':form,'taluk':taluk})
    # return render(request,'taluk.html',{'form':form,'taluk':taluk})



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
    if request.method == 'POST':
        form = SakhaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kvs_app:sakha')
    else:
        form = SakhaForm()
    if request.user.is_superuser:
        sakha = Sakha.objects.all().order_by('-id')
        return render(request,'sakha.html',{'form':form,'sakha':sakha})
    elif request.user.is_staff:
        district = request.user.extendedusermodel.district
        sakha = Sakha.objects.filter(district=district).order_by('-id')
        return render(request,'sakha.html',{'form':form,'sakha':sakha})
    else: 
        sakha = Sakha.objects.all().order_by('-id')
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
    if request.user.is_superuser:
        bride = Matrimonial.objects.filter(gender__name='Bride (വധു)',status='Approved').order_by('-id')
        return render(request,'materimonialservices.html',{'result':bride})
    elif request.user.is_staff:
        district = request.user.extendedusermodel.district
        bride = Matrimonial.objects.filter(gender__name='Bride (വധു)',status='Approved',district=district).order_by('-id')
        return render(request,'materimonialservices.html',{'result':bride})
    else:
        bride = Matrimonial.objects.filter(gender__name='Bride (വധു)',status='Approved').order_by('-id')
        return render(request,'materimonialservices.html',{'result':bride})


def grooms(request):
    if request.user.is_superuser:
        grooms = Matrimonial.objects.filter(gender__name='Groom (വരൻ)',status='Approved').order_by('-id')
        return render (request,'materimonialservices-grooms.html',{'result':grooms})
    elif request.user.is_staff:
        district = request.user.extendedusermodel.district
        grooms = Matrimonial.objects.filter(gender__name='Groom (വരൻ)',status='Approved',district=district).order_by('-id')
        return render (request,'materimonialservices-grooms.html',{'result':grooms})
    else:
        grooms = Matrimonial.objects.filter(gender__name='Groom (വരൻ)',status='Approved').order_by('-id')
        return render (request,'materimonialservices-grooms.html',{'result':grooms})


        



def pending(request):
    if request.user.is_superuser:
        pending = Matrimonial.objects.filter(status='Pending').order_by('-id')
        return render(request,'materimonialservices-pending.html',{'result':pending})
    elif request.user.is_staff:
        district = request.user.extendedusermodel.district
        pending = Matrimonial.objects.filter(status='Pending',district=district).order_by('-id')
        return render(request,'materimonialservices-pending.html',{'result':pending})
    else:
        pending = Matrimonial.objects.filter(status='Pending').order_by('-id')
        return render(request,'materimonialservices-pending.html',{'result':pending})



# def matrimonial_update(request,update_id):
#     if request.method == 'POST':
#         update = Matrimonial.objects.filter(id=update_id).first()
#         form = MatrimonialUpdateForm(request.POST,request.FILES,instance=update)
#         if form.is_valid():
#             form.save()
#             messages.success(request,'Succesfully Updated')
#             return redirect('kvs_app:index')
#     else:
#         update = Matrimonial.objects.filter(id=update_id).first()
#         form = MatrimonialUpdateForm(instance=update)
#     return render(request,'matrimony-update.html',{'form':form})







def matrimony_bride_search(request):
    Query = None
    result = None
    if request.user.is_superuser:
        if 'q' in request.GET:
            Query = request.GET.get('q')
            result = Matrimonial.objects.filter(Q(name__icontains=Query),gender__name='Bride',status='Approved')
        return render(request,'bride-search-result.html',{'result':result})
    if request.user.is_staff:
        district = request.user.extendedusermodel.district
        if 'q' in request.GET:
            Query = request.GET.get('q')
            result = Matrimonial.objects.filter(Q(name__icontains=Query),gender__name='Bride',status='Approved',district=district)
        return render(request,'bride-search-result.html',{'result':result})
    else:
        if 'q' in request.GET:
            Query = request.GET.get('q')
            result = Matrimonial.objects.filter(Q(name__icontains=Query),gender__name='Bride',status='Approved')
        return render(request,'bride-search-result.html',{'result':result})


def matrimony_grooms_search(request):
    Query = None
    result = None
    if request.user.is_superuser:
        if 'q' in request.GET:
            Query = request.GET.get('q')
            result = Matrimonial.objects.filter(Q(name__icontains=Query),gender__name='Groom',status='Approved')
        return render(request,'grooms-search-result.html',{'result':result})
    elif request.user.is_staff:
        district = request.user.extendedusermodel.district
        if 'q' in request.GET:
            Query = request.GET.get('q')
            result = Matrimonial.objects.filter(Q(name__icontains=Query),gender__name='Groom',status='Approved',district=district)
        return render(request,'grooms-search-result.html',{'result':result})
    else:
        if 'q' in request.GET:
            Query = request.GET.get('q')
            result = Matrimonial.objects.filter(Q(name__icontains=Query),gender__name='Groom',status='Approved')
        return render(request,'grooms-search-result.html',{'result':result})




def profile_details(request,details_id):
    details = Databank.objects.filter(id=details_id)
    return render(request,'viewprofile.html',{'details':details})




def databank_delete(request,dlt_id):
    dlt = Matrimonial.objects.filter(id=dlt_id)
    dlt.delete()
    return redirect('kvs_app:data_bank')


# def data_bank_register(request):
#     if request.method == 'POST':
#         form = MatrimonialForm(request.POST,request.FILES)
#         if form.is_valid():
#             data = form.save(commit=False)
#             year = form.cleaned_data['dob']
#             year = re.split(r'-',str(year))[0]
#             age = int(now.year)-int(year)
#             data.age = age
#             data.save()
#             print('UPDATED')
#             messages.success(request,'Please wait for the Admin approval')
#             return redirect('kvs_app:data_bank_register')
#     else:
#         form = MatrimonialForm()
#         print('NOT UPDATED')
#     return render(request,'marriageregister.html',{'form':form})


def data_bank_register(request):
    if request.method == 'POST':
        form = DatabankAddForm(request.POST,request.FILES)
        print(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            print('UPDATED')
            messages.success(request,'Please wait for the Admin approval')
            return redirect('kvs_app:data_bank_register')
    else:
        form = DatabankAddForm()
    return render(request,'marriageregister.html',{'form':form})


def data_bank(request):
    result = Databank.objects.filter(status = 'Unhide')
    return render(request,'data-bank.html',{'result':result})

def databank_update(request,update_id):
    if request.method == 'POST':
        update = Databank.objects.filter(id=update_id).first()
        form = DatabankEditForm(request.POST,request.FILES,instance=update)
        if form.is_valid():
            form.save()
            messages.success(request,'Succesfully Updated')
            return redirect('kvs_app:data_bank')
    else:
        update = Databank.objects.filter(id=update_id).first()
        form = DatabankEditForm(instance=update)
    return render(request,'matrimony-update.html',{'form':form})


def databank_delete(request,dlt_id):
    dlt = Databank.objects.filter(id=dlt_id)
    dlt.delete()
    messages.success(request,'Deleted..')
    return redirect('kvs_app:data_bank')


def data_bank_search(request):
    Query = None
    result = None
    if 'q' in request.GET:
        Query = request.GET.get('q')
        result = Databank.objects.filter(Q(name__icontains=Query),status = 'Unhide')
    return render(request,'bride-search-result.html',{'result':result})




def data_bank_hide(request):
    result = Databank.objects.filter(status = 'Hide')
    return render(request,'data-bank.html',{'result':result})




def health_insurance(request):
    if request.method == 'POST':
        form = Services_Add_Form(request.POST)
        if form.is_valid():
            form.save()
            print('success')
            messages.success(request,'Wait for the Admin Approval')
            return redirect('kvs_app:index')
    else:
        form = Services_Add_Form()
    if request.user.is_superuser:
        result = Services.objects.filter(category__name='Health Insurance',status='Approved').order_by('-id')
        return render(request,'health-insurance.html',{'form':form,'result':result})
    elif request.user.is_staff:
        district = request.user.extendedusermodel.district
        result = Services.objects.filter(category__name='Health Insurance',status='Approved',district=district).order_by('-id')
        return render(request,'health-insurance.html',{'form':form,'result':result})
    else:
        result = Services.objects.filter(category__name='Health Insurance',status='Approved').order_by('-id')
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
    if request.method == 'POST':
        form = Services_Add_Form(request.POST)
        if form.is_valid():
            form.save()
            print('success')
            messages.success(request,'Wait for the Admin Approval')
            return redirect('kvs_app:index')
    else:
        form = Services_Add_Form()
    if request.user.is_superuser:
        result = Services.objects.filter(category__name='Accident Insurance',status='Approved').order_by('-id')
    elif request.user.is_staff:
        district = request.user.extendedusermodel.district
        result = Services.objects.filter(category__name='Accident Insurance',status='Approved',district=district).order_by('-id')
    else:
        result = Services.objects.filter(category__name='Accident Insurance',status='Approved').order_by('-id')
    return render(request,'accident-insurance.html',{'form':form,'result':result})




def insurance_pending(request):
    if request.user.is_superuser:
        pending = Services.objects.filter(status='Pending').order_by('-id')
        return render(request,'insurance-pending.html',{'pending':pending})
    elif request.user.is_staff:
        district = request.user.extendedusermodel.district
        pending = Services.objects.filter(status='Pending',district=district).order_by('-id')
        return render(request,'insurance-pending.html',{'pending':pending})
    else:
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



# def join_kvs(request):
    
    if request.user.is_superuser:
        if request.method == 'POST':
            form = Join_Kvs_Add_Form(request.POST)
            if form.is_valid():
                data = form.save(commit=False)
                staff_name = User.objects.get(username=request.user.username)
                data.added_by = staff_name
                data.save()
                messages.success(request,'Membership will be Approved only after verification of Admin')
                return redirect('kvs_app:join_kvs')
        else:
            form = Join_Kvs_Add_Form()
        membership_list = Join_Kvs.objects.filter(status='Approved').order_by('-id')
        return render(request,'join-kvs.html',{'form':form,'membership_list':membership_list})
    elif request.user.is_staff:
        if request.method == 'POST':
            form = Join_Kvs_Add_Form(request.POST)
            if form.is_valid():
                data = form.save(commit=False)
                staff_name = User.objects.get(username=request.user.username)
                data.added_by = staff_name
                data.save()
                messages.success(request,'Membership will be Approved only after verification of Admin')
                return redirect('kvs_app:join_kvs')
        else:
            form = Join_Kvs_Add_Form()
        if request.user.extendedusermodel.district == 'Trivandrum':
            membership_list = Join_Kvs.objects.filter(status='Approved',district = 'Trivandrum').order_by('-id')
            return render(request,'join-kvs.html',{'form':form,'membership_list':membership_list})

    else:
        if request.method == 'POST':
            form = Join_Kvs_Add_Form(request.POST)
            if form.is_valid():
                data = form.save(commit=False)
                # staff_name = User.objects.get(username=request.user.username)
                # data.added_by = staff_name
                data.save()
                messages.success(request,'Membership will be Approved only after verification of Admin')
                return redirect('kvs_app:join_kvs')
        else:
            form = Join_Kvs_Add_Form()
        membership_list = Join_Kvs.objects.filter(status='Approved').order_by('-id')
        return render(request,'join-kvs.html',{'form':form,'membership_list':membership_list})


def join_kvs(request):
    if request.method == 'POST':
        form = Join_Kvs_Add_Form(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            username = request.user.username
            if username:
                staff_name = User.objects.get(username = username)
                data.added_by = staff_name
                data.save()
            else:
                data.save()
            messages.success(request,'Membership will be Approved only after verification of Admin')
            return redirect('kvs_app:join_kvs')
    else:
        form = Join_Kvs_Add_Form()
    if request.user.is_superuser:
        membership_list = Join_Kvs.objects.filter(status='Approved').order_by('-id')
        return render(request,'join-kvs.html',{'form':form,'membership_list':membership_list})
    elif request.user.is_staff:
        district = request.user.extendedusermodel.district
        membership_list = Join_Kvs.objects.filter(status='Approved',district=district).order_by('-id')
        return render(request,'join-kvs.html',{'form':form,'membership_list':membership_list})
    else:
        membership_list = Join_Kvs.objects.filter(status='Approved').order_by('-id')
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


def join_kvs_profile_view(request,join_kvs_id):
    kvs = Join_Kvs.objects.filter(id=join_kvs_id)
    return render (request,'join-kvs-profile-view.html',{'kvs':kvs})




def join_kvs_pending(request):
    if request.user.is_superuser:
        pending = Join_Kvs.objects.filter(status = 'Pending').order_by('-id')
    elif request.user.is_staff:
        district = request.user.extendedusermodel.district
        pending = Join_Kvs.objects.filter(status = 'Pending',district = district).order_by('-id')
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
            'Artisan Sevana Kendram', #subject
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


# REPORT SECTION (EXCEL)

def join_kvs_excel_report(request):
    # content-type of response
    response = HttpResponse(content_type='application/ms-excel')

    #decide file name
    response['Content-Disposition'] = 'attachment; filename="Join KVS Report.xls"'

    #creating workbook
    wb = xlwt.Workbook(encoding='utf-8')

    #adding sheet
    ws = wb.add_sheet("sheet1")

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    # headers are bold
    font_style.font.bold = True
    #column header names, you can use your own headers here
    columns = ['Name','Age','Dob','Sex','Address','Mobile','District','Union','Sakha No']

    #write column headers in sheet
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    
    data = Join_Kvs.objects.all().order_by('-id')
    # for i in data:
    #     print(i.state)
    
    # data1 = Leads.objects.filter(lead_source='Youtube').order_by('-date')
    # nonee = 'None'
    Male='M'
    Female = 'F'
    for my_row in data:
        row_num = row_num + 1
        ws.write(row_num, 0, my_row.name, font_style)
        ws.write(row_num, 1, my_row.age, font_style)
        ws.write(row_num, 2, my_row.dob, font_style)
        if my_row.sex == None:
            ws.write(row_num, 3, 'None', font_style)
        else:
            if my_row.sex.name == 'Male':
                ws.write(row_num, 3, Male, font_style)
            elif my_row.sex.name == 'Female':
                ws.write(row_num, 3, Female, font_style)
        ws.write(row_num, 4, my_row.address, font_style)
        ws.write(row_num, 5, my_row.mobile, font_style)
        ws.write(row_num, 6, my_row.district, font_style)
        if my_row.union == None:
            ws.write(row_num, 7, 'None', font_style)
        else:
            ws.write(row_num, 7, my_row.union.name, font_style)
        ws.write(row_num, 8, my_row.sakha_no, font_style)
        
    wb.save(response)
     
    return response




# ACCOUNT SECTION

def super_admin_register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")  
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print("username alredy exists")
                messages.info(request,"username already exist")
                return redirect("kvs_app:super_admin_register")
            elif User.objects.filter(email=email).exists():
                print("email alredy exists")
                messages.info(request,"email already registered")
                return redirect("kvs_app:super_admin_register")
            else:
                user = User.objects.create_user(username=username,email=email,password=password1,is_superuser=True,is_active=True,is_staff=True)
                user.save();
                print('user created')
                # # MESSAGE SENDING CODE
                # template = render_to_string('admin-register-email.html',{'emp_name':username})
                # email = EmailMessage(
                #     'Account Registration', #subject
                #     template, #body
                #     settings.EMAIL_HOST_USER, #sender mail id
                #     [email] #recever mail id
                # )
                # email.fail_silently = False
                # email.send()
                return redirect('kvs_app:login')
        else:
            print('Password Not Matched')
            messages.info(request,"Incorrect Password")
            return redirect('kvs_app:super_admin_register')    
    return render(request,"admin-register.html")


def district_admin_register(request):
    if request.method == 'POST':
        if request.POST.get('password1') == request.POST.get('password2'):
            try:
                user = User.objects.get(username=request.POST.get('username'))
                print('username already taken')
                return render(request,'district-admin-register.html',{'error':"Username alredy exist"})
                
            except User.DoesNotExist:
                user = User.objects.create_user(username = request.POST.get('username'), password = request.POST.get('password1'),email=request.POST.get('email'),is_staff=True)
                district = request.POST.get('district')
                extenduser = ExtendedUserModel(user = user , district = district)
                extenduser.save();
                print('user created')
                auth.login(request,user)
                # # MESSAGE SENDING CODE
                # template = render_to_string('resgisteremail.html',{'emp_name':emp_name,'emp_id':emp_id})
                # email = EmailMessage(
                #     'Account Registration', #subject
                #     template, #body
                #     settings.EMAIL_HOST_USER, #sender mail id
                #     [email] #recever mail id
                # )
                # email.fail_silently = False
                # email.send()
                return redirect('kvs_app:login')

        else:
            print('password not matching')
            return render(request,'district-admin-register.html',{'error':'Password Does Not Match'})
    else:
        return render(request,'district-admin-register.html')







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










