from django import forms
from .models import MyModel
from .models import Newbook

class MyForm(forms.ModelForm):
  class Meta:
    model = MyModel
    fields = ["bname", "bprice","author","story","image",]
    labels = {"bname": "Name", "brice": "price","author":"Author","story":"summary","image":"img",}
  class Meta:
    model = Newbook
    fields = ["images",]
    labels = {"images":"img",}