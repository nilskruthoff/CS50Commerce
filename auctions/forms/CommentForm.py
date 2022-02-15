from django import forms
from django.forms import ModelForm

from auctions.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment

        fields = ['title', 'comment']
        labels = {
            'title': 'Comment Title',
            'comment': 'Comment'
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-2'}),
            'comment': forms.Textarea(attrs={'class': 'form-control my-2'})
        }