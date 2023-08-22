from django.contrib import admin
from .models import Databank,ExtendedUserModel, Sex_Choices,StateCommitie,Taluk_choices,Taluk,Sakha,Matrimonial,SubCaste_choices,Gender_choices,Star,Insurence_category,Id_details_choices,Payment_details_choices,Services,Join_Kvs

# Register your models here.
admin.site.register(StateCommitie)
admin.site.register(Taluk_choices)
admin.site.register(Taluk)
admin.site.register(Sakha)
admin.site.register(Matrimonial)
admin.site.register(SubCaste_choices)
admin.site.register(Gender_choices)
admin.site.register(Star)
admin.site.register(Insurence_category)
admin.site.register(Id_details_choices)
admin.site.register(Payment_details_choices)
admin.site.register(Services)
admin.site.register(Join_Kvs)
admin.site.register(Sex_Choices)
admin.site.register(ExtendedUserModel)
admin.site.register(Databank)






