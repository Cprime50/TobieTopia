from django import forms

from .models import Comment, Contact

class CommentForm(forms.ModelForm):             #creating our commentform with django inbuilt forms system, also save form data in our database
    class Meta:                                 #inheriting the attributes of commentform class in our models.py
        model = Comment
        fields = ('name', 'email', 'body')

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')           #could also use '__all__' since  this basically inheriting all theattributes of the contact class in our models