from .models import Post, Comment
from django import forms


# class CommentForm(forms.ModelForm):
#     content = forms.CharField(widget=forms.Textarea)
#
#     class Meta:
#         model = Comment
#         fields = ('content',)