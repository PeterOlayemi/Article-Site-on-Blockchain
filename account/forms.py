from django import forms
from .models import Comment, Update

class CommentForm(forms.ModelForm):
    name=forms.CharField(max_length=50, help_text='Input Your Full Name', required=True)
    email=forms.EmailField(max_length=50, help_text='Input Your Email Address', required=True)
    comment=forms.Textarea()

    class Meta:
        model=Comment
        fields=['name','email','comment']

class UpdateForm(forms.ModelForm):
    name=forms.CharField(max_length=50, required=True)
    email=forms.EmailField(max_length=50, required=True)

    class Meta:
        model=Update
        fields=['name','email']