from .models import Comment
from django import forms


class UserCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user_name', 'email', 'body', )