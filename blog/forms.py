from .models import Post, Comment
from django import forms


class CommentForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows': 2, 'cols': 60}))

    class Meta:
        model = Comment
        fields = ('content',)
