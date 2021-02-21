from django.conf import settings
from allauth.account.forms import SignupForm
from captcha.fields import ReCaptchaField


class CaptchaSignupForm(SignupForm):
    # https://django-allauth.readthedocs.io/en/latest/forms.html
    captcha = ReCaptchaField()

    def save(self, request):
        user = super(CaptchaSignupForm, self).save(request)
        return user
