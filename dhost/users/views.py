from django.conf import settings
from django.contrib import messages
from django.contrib.auth import REDIRECT_FIELD_NAME, get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseRedirect
from django.shortcuts import resolve_url
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.http import url_has_allowed_host_and_scheme
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from .forms import AccountSettingsForm, SignupForm

User = get_user_model()


class TitleMixin:
    title = None
    extra_context = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'title': self.title, **(self.extra_context or {})})
        return context


class LoginView(auth_views.LoginView):
    template_name = 'users/login.html'


class LogoutView(auth_views.LogoutView):
    # TODO logout with POST
    template_name = 'users/logged_out.html'


class PasswordResetView(auth_views.PasswordResetView):
    email_template_name = 'users/emails/password_reset_email.html'
    subject_template_name = 'users/emails/password_reset_subject.txt'
    template_name = 'users/password_reset_form.html'


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'users/password_reset_confirm.html'


class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'users/password_reset_complete.html'


class PasswordChangeView(auth_views.PasswordChangeView):
    template_name = 'users/password_change_form.html'


class PasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    template_name = 'users/password_change_done.html'


class SignupView(TitleMixin, auth_views.SuccessURLAllowedHostsMixin, FormView):
    """
    Display the registration form and handle the register action.
    """
    form_class = SignupForm
    authentication_form = None
    next_page = None
    redirect_field_name = REDIRECT_FIELD_NAME
    template_name = 'users/signup.html'
    redirect_authenticated_user = False
    extra_context = None
    title = _('Sign up')

    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if (self.redirect_authenticated_user and
                self.request.user.is_authenticated):
            redirect_to = self.get_success_url()
            if redirect_to == self.request.path:
                raise ValueError(
                    "Redirection loop for authenticated user detected. Check "
                    "that your LOGIN_REDIRECT_URL doesn't point to a login "
                    "page.")
            return HttpResponseRedirect(redirect_to)
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return self.get_redirect_url() or self.get_default_redirect_url()

    def get_redirect_url(self):
        """Return the user-originating redirect URL if it's safe."""
        redirect_to = self.request.POST.get(
            self.redirect_field_name,
            self.request.GET.get(self.redirect_field_name, ''))
        url_is_safe = url_has_allowed_host_and_scheme(
            url=redirect_to,
            allowed_hosts=self.get_success_url_allowed_hosts(),
            require_https=self.request.is_secure(),
        )
        return redirect_to if url_is_safe else ''

    def get_default_redirect_url(self):
        """Return the default redirect URL."""
        return resolve_url(self.next_page or settings.LOGIN_REDIRECT_URL)

    def get_form_class(self):
        return self.authentication_form or self.form_class

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        form.save()
        auth_login(
            self.request,
            form.get_user(),
            backend='django.contrib.auth.backends.ModelBackend',
        )
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_site = get_current_site(self.request)
        context.update({
            self.redirect_field_name: self.get_redirect_url(),
            'site': current_site,
            'site_name': current_site.name,
            **(self.extra_context or {})
        })
        return context


class AccountSettingsView(TitleMixin, FormView):
    template_name = 'users/account_settings.html'
    form_class = AccountSettingsForm
    success_url = reverse_lazy('account_settings')
    title = _('Account settings')

    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_protect)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Account successfully updated',
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'An error occured, please try again later',
        )
        return super().form_invalid(form)


class AccountDeleteView(TitleMixin, TemplateView):
    template_name = 'users/account_delete.html'
    success_url = reverse_lazy('account_delete_done')
    title = _('Delete account')

    @method_decorator(csrf_protect)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Delete the user's account on a POST
        """
        user = request.user
        user.delete()
        messages.add_message(
            request,
            messages.SUCCESS,
            'Account successfully deleted',
        )
        return HttpResponseRedirect(str(self.success_url))


class AccountDeleteDoneView(TitleMixin, TemplateView):
    template_name = 'users/account_delete_done.html'
    title = _('Delete account successful')
