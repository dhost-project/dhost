from captcha.fields import ReCaptchaField
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.forms import ModelForm

User = get_user_model()


class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username',)
        field_classes = {'username': UsernameField}

    def __init__(self, *args, **kwargs):
        self.user = None
        return super().__init__(*args, **kwargs)

    def save(self, commit=True):
        user = super().save(commit=commit)
        self.user = user
        return user

    def get_user(self):
        return self.user


class CaptchaSignupForm(SignupForm):
    captcha = ReCaptchaField()

    def save(self, request):
        user = super(CaptchaSignupForm, self).save(request)
        return user


class AccountSettingsForm(ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
