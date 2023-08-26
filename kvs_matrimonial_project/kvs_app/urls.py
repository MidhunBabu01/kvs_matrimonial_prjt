from django.urls import path
from kvs_app import views

app_name = 'kvs_app'
urlpatterns = [
    path('', views.index,name='index'),
    path('executiveforum', views.executiveforum,name='executiveforum'),
    path('executive-forum-update/<int:update_id>',views.executiveforum_update,name='executiveforum_update'),
    path('delete/<int:dlt_id>',views.executiveforum_delete,name='executiveforum_delete'),
    path('taluk', views.taluk,name='taluk'),
    path('taluk-update/<int:taluk_id>', views.taluk_update,name='taluk_update'),
    path('taluk_delete/<int:taluk_id>', views.taluk_delete,name='taluk_delete'),
    path('sakha', views.sakha,name='sakha'),
    path('sakha-update/<int:sakha_id>', views.sakha_update,name='sakha_update'),
    path('sakha-delete/<int:sakha_id>', views.sakha_delete,name='sakha_delete'),
    path('matrimonial-service-bride', views.bride,name='bride'),
    path('matrimonial-service-grooms', views.grooms,name='grooms'),
    path('matrimonial-service-pending', views.pending,name='pending'),
    path('profile-details/<int:details_id>', views.profile_details,name='profile_details'),
    # path('marrige-register', views.marrige_register,name='marrige_register'),
    path('data-bank-register', views.data_bank_register,name='data_bank_register'),
    path('data-bank', views.data_bank,name='data_bank'),
    path('databank-update/<int:update_id>', views.databank_update,name='databank_update'),
    path('databank-delete/<int:dlt_id>', views.databank_delete,name='databank_delete'),
    path('data-bank-search', views.data_bank_search,name='data_bank_search'),
    path('data-bank-hide', views.data_bank_hide,name='data_bank_hide'),
    
    path('contact', views.contact,name='contact'),
    path('matrimoni-delete/<int:dlt_id>', views.databank_delete,name='databank_delete'),
    # path('matrimonial-update', views.matrimonial_update,name='matrimonial_update'),
    # path('matrimonial-update/<int:update_id>', views.matrimonial_update,name='matrimonial_update'),
    path('matrimony-bride-search', views.matrimony_bride_search,name='matrimony_bride_search'),
    path('matrimony-groom-search', views.matrimony_grooms_search,name='matrimony_grooms_search'),
    path('health-insurance', views.health_insurance,name='health_insurance'),
    # path('services-update/<int:update_id>', views.health_insurance_update,name='health_insurance_update'),
    path('insurance_delete/<int:dlt_id>', views.insurance_delete,name='insurance_delete'),
    path('accident-insurance', views.accident_insurance,name='accident_insurance'),
    path('insurance-pending', views.insurance_pending,name='insurance_pending'),
    path('insurance-update/<int:update_id>', views.insurance_update,name='insurance_update'),
    path('join-ask', views.join_kvs,name='join_kvs'),
    path('join-kvs-delete/<int:dlt_id>', views.join_kvs_delete,name='join_kvs_delete'),
    path('join-kvs-update/<int:update_id>', views.join_kvs_update,name='join_kvs_update'),
    path('join-kvs-profile-view/<int:join_kvs_id>', views.join_kvs_profile_view,name='join_kvs_profile_view'),
    path('join-kvs-pending', views.join_kvs_pending,name='join_kvs_pending'),
    # EXCEL REPORT
    path('join-kvs-excel-report', views.join_kvs_excel_report,name='join_kvs_excel_report'),
    
    
    # ACCOUNT SECTION
    path('super-admin-register', views.super_admin_register,name='super_admin_register'),
    path('district-admin-register', views.district_admin_register,name='district_admin_register'),
     
    path('login', views.login,name='login'),
    path('logout', views.logout,name='logout'),
    
    


]
