from django import forms
from .models import CodePen

class CodePenForm(forms.ModelForm):
    class Meta:
        model = CodePen
        fields = ['html_code', 'css_code', 'js_code']
