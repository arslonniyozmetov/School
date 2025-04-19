# forms.py
from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'contact_info', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ismingiz'}),
            'contact_info': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon raqam yoki Email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Xabaringizni yozing', 'rows': 4}),
        }
