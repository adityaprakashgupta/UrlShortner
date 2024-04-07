# make model form for Url model
# imports
from django import forms
from .models import Url


# create model form
class UrlForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = ['original_url']
        labels = {
            'original_url': 'Enter URL to shorten'
        }
        widgets = {
            'original_url': forms.URLInput(attrs={'class': 'form-control'})
        }
