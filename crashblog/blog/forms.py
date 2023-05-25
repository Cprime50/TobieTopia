from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):             #creating our comment with django inbuilt forms system
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')