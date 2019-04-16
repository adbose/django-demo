from django import forms

class FeedbackForm(forms.Form):
    full_name = forms.CharField()
    email = forms.CharField()
    message = forms.CharField()
