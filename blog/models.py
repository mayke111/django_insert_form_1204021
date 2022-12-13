from django import forms
from django.db.models import Model, CharField, TextField


class Post(Model):
    title = CharField(max_length=255)
    blog = TextField()
    # creator = CharField(max_length=40)


class PostForm(forms.Form):
    title = forms.CharField(required=True, max_length=100)
    blog = forms.CharField(required=True, min_length=9, widget=forms.Textarea)

    class Meta:
        model = Post
        field = ['title', 'blog']

# Create your models here.
