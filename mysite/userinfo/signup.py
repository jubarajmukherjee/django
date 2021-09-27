from django import forms
from .models import MyModel
 
class MyForm(forms.ModelForm):
  class Meta:
    model = MyModel
    fields = ["uname", "email", "password", "cpassword", "address",]
    labels = {'uname': "UserName", "email": "E-Mail","password": "Password","cpassword": "Re-Password","address": "Address",}