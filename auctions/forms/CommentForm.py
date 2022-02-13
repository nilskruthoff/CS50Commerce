from django.forms import ModelForm
from django import forms
from auctions.models import CommentModel


class CommentForm(ModelForm):
    class Meta:
        model = CommentModel

        fields = ['title', 'comment']
        labels = {
            'title': 'Comment Title',
            'comment': 'Comment'
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-2'}),
            'comment': forms.Textarea(attrs={'class': 'form-control my-2'})
        }