from captcha.fields import ReCaptchaField
from django.conf import settings


class SignupForm:
    pass


class CaptchaSignupForm(SignupForm):
    captcha = ReCaptchaField()

    def save(self, request):
        user = super(CaptchaSignupForm, self).save(request)
        return user
