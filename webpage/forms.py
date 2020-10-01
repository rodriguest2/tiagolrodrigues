from django import forms
from django.core import validators
from webpage.models import Post, Category, Comment
from webpage.cat import cat_list




class PostForm(forms.ModelForm):

    class Meta():
        model=Post
        fields=('title','category','body','post_img')

        widgets={
            'title':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Title'
            }),
            'body':forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'Blog Body',
                'rows':25
            }),
            'category':forms.Select(choices=cat_list,attrs={
                'class':'form-control',
            }),
        }



class CommentForm(forms.ModelForm):

    class Meta():
        model=Comment
        fields=('name','body')

        widgets={
            'name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Name',
            }),
            'body':forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'Comment',
                'rows':25
            }),
        }



class ContactForm(forms.Form):
    name=forms.CharField(
        max_length=100,
        required=True,
        label='Name',
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Name'
            })
        )

    email=forms.EmailField(
        max_length=100,
        required=True,
        label='Email',
        widget=forms.EmailInput(attrs={
            'class':'form-control',
            'placeholder':'Email'
            })
        )

    phone=forms.CharField(
        max_length=13,
        required=False,
        label='Phone',
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Phone (optional)'
            })
        )

    message=forms.CharField(
        max_length=1000,
        required=True,
        label='Message',
        widget=forms.Textarea(attrs={
            'class':'form-control',
            'placeholder':'Message'
            })
        )

    botcatcher=forms.CharField(
        required=False,
        widget=forms.HiddenInput,
        validators=[validators.MaxLengthValidator(0)],
        label='bot'
        )
