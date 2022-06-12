from .models import *
from django.forms import ModelForm

class upload_form(ModelForm): # inherit from ModelForm
    
    class Meta:
        model = upload_file
        fields = ['file']