from django import forms
from .models import Databank, Join_Kvs, StateCommitie,Taluk,Sakha,Matrimonial,Services




class StateCommiteForm(forms.ModelForm):
    class Meta:
        model = StateCommitie
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'phone' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Mobile'}),
            'place' : forms.TextInput(attrs={'class':'form-control','placeholder':'Place'}),
            'photo' : forms.ClearableFileInput(attrs={'class':'form-control'}),
        }



class TalukForm(forms.ModelForm):
    class Meta:
        model = Taluk
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'phone' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Mobile'}),
            'district': forms.Select(attrs={'class':'form-control','placeholder':'District'}),
            'taluk' : forms.Select(attrs={'class':'form-control','placeholder':'Place'})
        }




class SakhaForm(forms.ModelForm):
    class Meta:
        model = Sakha
        fields = '__all__'
        widgets = {
            'sakha_no' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Sakha Number'}),
            'district': forms.Select(attrs={'class':'form-control'}),
            'taluk' : forms.Select(attrs={'class':'form-control','placeholder':'Taluk'}),
            'sakaha_name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Sakha Name'}),
        }



# class MatrimonialForm(forms.ModelForm):
#     class Meta:
#         model = Matrimonial
#         fields = '__all__'
#         exclude = ['created_at','age','status']
#         widgets = {
#             'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name'}),
#             'dob' : forms.DateInput(attrs={'class':'form-control','type':'date'}),
#             'phone' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Mobile'}),
#             'email' : forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email'}),
#             'gender' : forms.Select(attrs={'class':'form-control'}),
#             'height' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Height in CM'}),
#             'work_place' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Work place'}),
#             'languages' : forms.TextInput(attrs={'class':'form-control','placeholder':'Languages Known'}),
#             'hobbies' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Hobbies'}),
#             'brother' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter The Number of Brothers'}),
#             'district' : forms.Select(attrs={'class':'form-control','placeholder':'Enter District'}),
#             'star' : forms.Select(attrs={'class':'form-control'}),
#             'gaurdian_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Gaurdian Name'}),
#             # 'gaurdian_mobile': forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Gaurdian Mobile'}),
#             'father_name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Father Name'}),
#             'father_occupation' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Father Occupation'}),
#             'mother_name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Mother Name'}),
#             'mother_occupation' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Mother Occupation'}),
#             'sister' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter The Number of Sisters'}),
#             'total_family_members' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Number of Total family members'}),
#             'marital_status' : forms.Select(attrs={'class':'form-control'}),
#             'subcaste' : forms.Select(attrs={'class':'form-control'}),
#             'education_qualification' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Qualification'}),
#             'occupation' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Occupation'}),
#             'taluk' : forms.TextInput(attrs={'class':'form-control'}),
#             # 'status' : forms.Select(attrs={'class':'form-control'}),

#         }


class DatabankAddForm(forms.ModelForm):
    class Meta:
        model = Databank
        fields = '__all__'
        exclude = ['status']
        widgets = {
            'category' : forms.TextInput(attrs={'class':'form-control'}),
            'name' : forms.TextInput(attrs={'class':'form-control',}),
            'mobile' : forms.NumberInput(attrs={'class':'form-control'}),
            'photo' : forms.ClearableFileInput(attrs={'class':'form-control'}),
            'occupation' : forms.TextInput(attrs={'class':'form-control'}),
            'district' : forms.TextInput(attrs={'class':'form-control'}),
            'taluk' : forms.TextInput(attrs={'class':'form-control'}),
            'workplace' : forms.TextInput(attrs={'class':'form-control'}),
            'contact_person' : forms.TextInput(attrs={'class':'form-control'}),
        }

class DatabankEditForm(forms.ModelForm):
    class Meta:
        model = Databank
        fields = '__all__'
        widgets = {
            'category' : forms.TextInput(attrs={'class':'form-control'}),
            'name' : forms.TextInput(attrs={'class':'form-control',}),
            'mobile' : forms.NumberInput(attrs={'class':'form-control'}),
            'photo' : forms.ClearableFileInput(attrs={'class':'form-control'}),
            'occupation' : forms.TextInput(attrs={'class':'form-control'}),
            'district' : forms.TextInput(attrs={'class':'form-control'}),
            'taluk' : forms.TextInput(attrs={'class':'form-control'}),
            'workplace' : forms.TextInput(attrs={'class':'form-control'}),
            'contact_person' : forms.TextInput(attrs={'class':'form-control'}),
            'status' : forms.Select(attrs={'class':'form-control'})
        }













class MatrimonialUpdateForm(forms.ModelForm):
    class Meta:
        model = Matrimonial
        fields = '__all__'
        exclude = ['created_at','age']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name'}),
            'dob' : forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'phone' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Mobile'}),
            'email' : forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email'}),
            'gender' : forms.Select(attrs={'class':'form-control'}),
            'height' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Height in CM'}),
            'work_place' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Work place'}),
            'star' : forms.Select(attrs={'class':'form-control'}),
            'languages' : forms.TextInput(attrs={'class':'form-control','placeholder':'Languages Known'}),
            'hobbies' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Hobbies'}),
            'brother' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter The Number of Brothers'}),
            'district' : forms.Select(attrs={'class':'form-control','placeholder':'Enter District'}),
            'father_name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Father Name'}),
            'father_occupation' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Father Occupation'}),
            'mother_name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Mother Name'}),
            'gaurdian_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Gaurdian Name'}),
            'mother_occupation' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Mother Occupation'}),
            'sister' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter The Number of Sisters'}),
            'total_family_members' : forms.NumberInput(attrs={'class':'form-control'}),
            'marital_status' : forms.Select(attrs={'class':'form-control'}),
            'subcaste' : forms.Select(attrs={'class':'form-control'}),
            'education_qualification' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Qualification'}),
            'occupation' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Occupation'}),
            'taluk' : forms.TextInput(attrs={'class':'form-control'}),
            'status' : forms.Select(attrs={'class':'form-control'}),

        }



class Services_Add_Form(forms.ModelForm):
    class Meta:
        model = Services
        fields = '__all__'
        exclude = ['status']
        widgets = {
            'category' : forms.Select(attrs={'class':'form-control'}),
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'mobile_no' : forms.NumberInput(attrs={'class':'form-control'}),
            'joining_date' : forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'id_details' : forms.Select(attrs={'class':'form-control'}),
            'id_no' : forms.TextInput(attrs={'class':'form-control'}),
            'sakha_no' : forms.TextInput(attrs={'class':'form-control'}),
            'district' : forms.Select(attrs={'class':'form-control'}),
            'taluk' : forms.TextInput(attrs={'class':'form-control'}),
            'payment_details' : forms.Select(attrs={'class':'form-control'}),
            'proposed_by_name' : forms.TextInput(attrs={'class':'form-control'}),
            'proposed_by_contact_no' : forms.NumberInput(attrs={'class':'form-control'}),
            # 'status': forms.Select(attrs={'class':'form-control'}),
            
        }




class Services_Admin_Edit_Form(forms.ModelForm):
    class Meta:
        model = Services
        fields = '__all__'
        widgets = {
            'category' : forms.Select(attrs={'class':'form-control'}),
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'mobile_no' : forms.NumberInput(attrs={'class':'form-control'}),
            'joining_date' : forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'id_details' : forms.Select(attrs={'class':'form-control'}),
            'id_no' : forms.TextInput(attrs={'class':'form-control'}),
            'sakha_no' : forms.TextInput(attrs={'class':'form-control'}),
            'taluk' : forms.TextInput(attrs={'class':'form-control'}),
            'district' : forms.Select(attrs={'class':'form-control'}),
            'payment_details' : forms.Select(attrs={'class':'form-control'}),
            'proposed_by_name' : forms.TextInput(attrs={'class':'form-control'}),
            'proposed_by_contact_no' : forms.NumberInput(attrs={'class':'form-control'}),
            'status' : forms.Select(attrs={'class':'form-control'})
            
        }


class Join_Kvs_Add_Form(forms.ModelForm):
    class Meta:
        model = Join_Kvs
        fields = '__all__'
        exclude = ['status']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'sex': forms.Select(attrs={'class':'form-control'}),
            'age': forms.NumberInput(attrs={'class':'form-control'}),
            'dob' : forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'mobile': forms.NumberInput(attrs={'class':'form-control'}),
            'address': forms.Textarea(attrs={'class':'form-control','rows':4}),
            'place': forms.TextInput(attrs={'class':'form-control'}),
            'taluk': forms.TextInput(attrs={'class':'form-control'}),
            'district': forms.Select(attrs={'class':'form-control'}),
            'union': forms.Select(attrs={'class':'form-control'}),
            'sakha_no': forms.TextInput(attrs={'class':'form-control'}),
            'id_proof': forms.Select(attrs={'class':'form-control'}),
            'id_proof_no': forms.TextInput(attrs={'class':'form-control'}),
            'membership_no': forms.TextInput(attrs={'class':'form-control'}),
            'payment_details': forms.Select(attrs={'class':'form-control'}),

        }


class Join_Kvs_Admin_Update(forms.ModelForm):
    class Meta:
        model = Join_Kvs
        fields = '__all__'
        exclude = ['added_by']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'sex': forms.Select(attrs={'class':'form-control'}),
            'age': forms.NumberInput(attrs={'class':'form-control'}),
            'dob' : forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'mobile': forms.NumberInput(attrs={'class':'form-control'}),
            'address': forms.Textarea(attrs={'class':'form-control','rows':4}),
            'place': forms.TextInput(attrs={'class':'form-control'}),
            'district': forms.Select(attrs={'class':'form-control'}),
            'union': forms.Select(attrs={'class':'form-control'}),
            'sakha_no': forms.TextInput(attrs={'class':'form-control'}),
            'id_proof': forms.Select(attrs={'class':'form-control'}),
            'id_proof_no': forms.TextInput(attrs={'class':'form-control'}),
            'membership_no': forms.TextInput(attrs={'class':'form-control'}),
            'status': forms.Select(attrs={'class':'form-control'}),
            'payment_details': forms.Select(attrs={'class':'form-control'}),

        }