from .models import CommentArticle
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentArticle
        fields = ('avtor_comment', 'text_comment',)
