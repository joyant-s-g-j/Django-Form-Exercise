from django import forms
# from django.core import validators

class DummyForm(forms.Form):
    name = forms.CharField(max_length=40)
    email = forms.EmailField()
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))