from django import forms


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