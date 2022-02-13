from django import forms

from home.models import ContactMessage, Comment_blog, NewsLatter


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name',  'subject','email','message', 'phone']


class Comment_detail_Form(forms.ModelForm):
    class Meta:
        model = Comment_blog
        fields = ( 'name', 'email', 'comment',)


class NewsLatterForm(forms.ModelForm):
    class Meta:
        model = NewsLatter
        fields = ( 'email',)
