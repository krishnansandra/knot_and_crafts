from django import forms
from .models import ContactMessage
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title','slug', 'category', 'description', 'price','image']

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows':4}),
        }
