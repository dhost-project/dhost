from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.forms import ModelForm

User = get_user_model()


class SignupForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        self.user = None
        return super().__init__(*args, **kwargs)

    def save(self, commit=True):
        user = super().save(commit=commit)
        self.user = user
        return self.user

    def get_user(self):
        return self.user


class AccountSettingsForm(ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'avatar')
        field_classes = {'username': UsernameField}
