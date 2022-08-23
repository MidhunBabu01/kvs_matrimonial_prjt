from django.contrib import admin
from .models import StateCommitie,Taluk_choices,Taluk,Sakha

# Register your models here.
admin.site.register(StateCommitie)
admin.site.register(Taluk_choices)
admin.site.register(Taluk)
admin.site.register(Sakha)