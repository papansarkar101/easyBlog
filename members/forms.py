from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from home.models import Profile

class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'website', 'facebook', 'twitter', 'instagram')

        widgets = {
                'bio': forms.Textarea(attrs={'class': 'form-control'}),
                # 'profile_pic': forms.FileField(attrs={'class': 'form-control'}),
                'website': forms.TextInput(attrs={'class': 'form-control'}),
                'facebook': forms.TextInput(attrs={'class': 'form-control'}),
                'twitter': forms.TextInput(attrs={'class': 'form-control'}),
                'instagram': forms.TextInput(attrs={'class': 'form-control'}),
            }

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=False, widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',
                  'username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditPersonalInfoForm(UserChangeForm):
    email = forms.EmailField(required=False, widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=16, required=False, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(max_length=16, required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(max_length=16, required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')