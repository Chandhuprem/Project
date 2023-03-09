from django import forms
from .models import Store
class myform(forms.ModelForm):
    class Meta:
        model=Store
    
        fields=["username","email","phone","bookname","Authorname"]
        labels={"username":"user","email":"email1","phone":"phone","bookname":"bname","Authorname":"aname"}