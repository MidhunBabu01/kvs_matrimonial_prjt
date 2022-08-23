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
    path('matrimonial-service', views.matrimonial_service,name='matrimonial_service'),
    path('profile-details', views.profile_details,name='profile_details'),
    path('marrige-register', views.marrige_register,name='marrige_register'),
    path('contact', views.contact,name='contact'),
    
    

    # ACCOUNT SECTION
    path('logout', views.logout,name='logout'),
    


]
