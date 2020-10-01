from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

class UserRegForm(UserCreationForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={
            'class':'form-control',
            'placeholder':'Email'
            })
        )
    first_name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'First Name'
            })
        )
    last_name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Last Name'
            })
        )

    class Meta():
        model=User
        fields=('username','first_name','last_name','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super(UserRegForm,self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Retype Password'



class ProfileForm(UserChangeForm):
    username=forms.CharField(max_length=100, widget=forms.TextInput(attrs={
            'class':'form-control',
            })
        )
    first_name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={
            'class':'form-control',
            })
        )
    last_name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={
            'class':'form-control',
            })
        )
    email=forms.EmailField(widget=forms.EmailInput(attrs={
            'class':'form-control',
            })
        )

    class Meta():
        model=User
        fields=('username','first_name','last_name','email',)



class PasswordForm(PasswordChangeForm):
    old_password=forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
            'class':'form-control',
            'placeholder':'Old Password'
            })
        )
    new_password1=forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
            'class':'form-control',
            'placeholder':'New Password'
            })
        )
    new_password2=forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
            'class':'form-control',
            'placeholder':'Retype New Password'
            })
        )

    class Meta():
        model=User
        fields=('old_password','new_password1','newpassword2')
