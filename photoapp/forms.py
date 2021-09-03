from .models import photo
from django import forms
class ModeForm(forms.ModelForm):
    class Meta:
        model=photo
        fields=['tittle','des','img']