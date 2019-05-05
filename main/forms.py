from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from main.models import Ticket


class SignupForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    venmo = forms.CharField(label='Venmo Handle (without @)')

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'venmo')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.venmo = self.cleaned_data['venmo']
        if commit:
            user.save()
        return user


class SellForm(forms.ModelForm):
    class Meta:
        model = Ticket
        exclude = ('seller',)

    def __init__(self, *args, **kwargs):
        self.seller = kwargs.pop('user')
        super(SellForm, self).__init__(*args, **kwargs)
