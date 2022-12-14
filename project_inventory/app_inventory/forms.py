from django import forms
from .models import appuser,items

class Itemcreateform(forms.ModelForm):
    class Meta:
        fields= ("title","particulars","lf","price","quantity","total")
        model=items
class userregistrationform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        fields=("full_name","contact","email","password")
        model=appuser
class userloginform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        fields=("email","password")
        model=appuser
