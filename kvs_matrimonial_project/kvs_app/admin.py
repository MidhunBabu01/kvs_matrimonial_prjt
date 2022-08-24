from django.contrib import admin
from .models import StateCommitie,Taluk_choices,Taluk,Sakha,Matrimonial,SubCaste_choices,Gender_choices

# Register your models here.
admin.site.register(StateCommitie)
admin.site.register(Taluk_choices)
admin.site.register(Taluk)
admin.site.register(Sakha)
admin.site.register(Matrimonial)
admin.site.register(SubCaste_choices)
admin.site.register(Gender_choices)