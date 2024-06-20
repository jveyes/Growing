from django import forms
from bootstrap5.forms import BootstrapFormMixin

class ContactForm(forms.Form, BootstrapFormMixin):
    name = forms.CharField(label='Your Name')
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(label='Your Message', widget=forms.Textarea)