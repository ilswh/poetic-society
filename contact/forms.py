from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Form to allow people to contact.
    """
    class Meta:
        model = Contact
        fields = "__all__"
