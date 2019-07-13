from django import forms

class ContactForm(forms.Form):
    name =forms.CharField(label='Your name',max_length=20)
    email =forms.EmailField(label='Your name')
    phone=forms.CharField(label='Your name',max_length=11)
    text=forms.CharField(label='Your name',max_length=200,widget=forms.Textarea)