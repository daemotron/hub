from django import forms
from captcha.fields import CaptchaField, CaptchaTextInput
from .validators import fse_username_validator


class ContactForm(forms.Form):
    name = forms.CharField(label='', max_length='100', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter your name',
            'aria-describedby': 'nameHelpBlock'
        }
    ))
    email = forms.EmailField(label='Your email address', widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email',
            'aria-describedby': 'emailHelpBlock'
        }
    ))
    message = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter your message',
            'aria-describedby': 'messageHelpBlock'
        }
    ))
    captcha = CaptchaField(widget=CaptchaTextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter captcha text'
        }
    ))


class RegisterForm(forms.Form):
    username = forms.CharField(
        label='Your FSE Game World username',
        max_length=150,
        validators=[fse_username_validator],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your FSE Game World username',
                'aria-describedby': 'usernameHelpBlock'
            }
        )
    )
    email = forms.EmailField(label='Your email address', widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email',
            'aria-describedby': 'emailHelpBlock'
        }
    ))
    password = forms.CharField(label='Chose a password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Chose a password',
            'aria-describedby': 'passwordHelpBlock'
        }
    ))
    pwrepeat = forms.CharField(label='Confirm your password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Retype your password',
            'aria-describedby': 'passwordRepeatHelpBlock'
        }
    ))
    captcha = CaptchaField(widget=CaptchaTextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter captcha text'
        }
    ))

    def clean(self):
        super().clean()
        password = self.cleaned_data.get('password')
        pwrepeat = self.cleaned_data.get('pwrepeat')
        if password != pwrepeat:
            msg = "Passwords must match each other."
            self.add_error('password', msg)
            self.add_error('pwrepeat', msg)


class ProfileForm(forms.Form):
    token = forms.UUIDField(label='Token', required=False, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter validation token'
        }
    ))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
        }
    ))
    avatar = forms.URLField(label='Avatar URL', required=False, widget=forms.URLInput(
        attrs={
            'class': 'form-control'
        }
    ))
    password = forms.CharField(label='New Password', required=False, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter new password',
        }
    ))
    pwrepeat = forms.CharField(label='Confirm Password', required=False, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Retype new password',
        }
    ))

    def clean(self):
        super().clean()
        password = self.cleaned_data.get('password')
        pwrepeat = self.cleaned_data.get('pwrepeat')
        if password and password != pwrepeat:
            msg = "Passwords must match each other."
            self.add_error('password', msg)
            self.add_error('pwrepeat', msg)
