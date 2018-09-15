from django import forms


class SettingForm(forms.Form):
    key = forms.CharField(label='', max_length='100', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter key',
            'aria-describedby': 'keyHelpBlock'
        }
    ))
    value = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter value expression'
        }
    ))
