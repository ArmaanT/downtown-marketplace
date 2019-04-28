from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


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
