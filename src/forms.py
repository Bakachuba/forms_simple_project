from django import forms

from src.models import GeeksModel


#without db
# class InputForm(forms.Form):
#     first_name = forms.CharField(max_length=200)
#     last_name = forms.CharField(max_length=200)
#     roll_number = forms.IntegerField(
#         help_text='Enter 6 digit roll number'
#     )
#     password = forms.CharField(widget=forms.PasswordInput())


class GeeksForm(forms.ModelForm):
    class Meta:
        model = GeeksModel
        fields = '__all__'