from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment  # Assuming the Comment model is in the blog app
        fields = ['author', 'content']
        # exclude = ()