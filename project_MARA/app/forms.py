from .models import *
from django import forms


class upload_form(forms.ModelForm):

    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True, 'class': 'form-control'}))


    class Meta:
        model = upload_file
        fields = ['file']
