from django import forms
from .models import StateCommitie,Taluk,Sakha




class StateCommiteForm(forms.ModelForm):
    class Meta:
        model = StateCommitie
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'phone' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Mobile'}),
            'place' : forms.TextInput(attrs={'class':'form-control','placeholder':'Place'})
        }



class TalukForm(forms.ModelForm):
    class Meta:
        model = Taluk
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'phone' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Mobile'}),
            'taluk' : forms.Select(attrs={'class':'form-control','placeholder':'Place'})
        }




class SakhaForm(forms.ModelForm):
    class Meta:
        model = Sakha
        fields = '__all__'
        widgets = {
            'sakha_no' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Sakha Number'}),
            'taluk' : forms.Select(attrs={'class':'form-control','placeholder':'Taluk'})
        }