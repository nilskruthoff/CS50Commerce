from django import forms
from django.forms import ModelForm

from auctions.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment

        fields = ['title', 'comment']
        labels = {
            'title': '',
            'comment': ''
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'Comment Title'}),
            'comment': forms.Textarea(attrs={'class': 'form-control my-2', 'placeholder': 'Comment'})
        }