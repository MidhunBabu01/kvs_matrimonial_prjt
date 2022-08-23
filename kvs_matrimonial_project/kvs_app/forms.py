from django import forms
from .models import StateCommitie




class StateCommiteForm(forms.ModelForm):
    class Meta:
        model = StateCommitie
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'phone' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Mobile'}),
            'place' : forms.TextInput(attrs={'class':'form-control','placeholder':'Place'})
        }