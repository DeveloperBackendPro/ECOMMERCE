from django import forms
from product.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [  'name', 'email', 'rate', 'subject', 'comment',]