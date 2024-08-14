from django import forms
from .models import AliasedUrl

class AliasedUrlForm(forms.ModelForm):
    class Meta:
        model = AliasedUrl
        fields = ['url']
