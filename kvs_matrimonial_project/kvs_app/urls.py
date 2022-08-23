from django.urls import path
from kvs_app import views

app_name = 'kvs_app'
urlpatterns = [
    path('', views.index,name='index'),
    path('executiveforum', views.executiveforum,name='executiveforum'),
    path('executive-forum-update/<int:update_id>',views.executiveforum_update,name='executiveforum_update'),
    path('delete/<int:dlt_id>',views.executiveforum_delete,name='executiveforum_delete'),
    path('taluk', views.taluk,name='taluk'),
    path('sakha', views.sakha,name='sakha'),
    path('matrimonial-service', views.matrimonial_service,name='matrimonial_service'),
    path('profile-details', views.profile_details,name='profile_details'),
    path('marrige-register', views.marrige_register,name='marrige_register'),
    path('contact', views.contact,name='contact'),
    
    

    # ACCOUNT SECTION
    path('logout', views.logout,name='logout'),
    


]
