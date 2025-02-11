from allauth.account.views import ConfirmEmailView, PasswordResetDoneView, PasswordResetFromKeyView, PasswordResetFromKeyDoneView, PasswordResetView, LoginView, SignupView
from news.views import BaseMixin


# Кастомные представления с BaseMixin
class CustomConfirmEmailView(BaseMixin, ConfirmEmailView):
    template_name = 'account/confirm_email.html'


class CustomPasswordResetDoneView(BaseMixin, PasswordResetDoneView):
    template_name = 'account/password_reset_done.html'


class CustomLoginView(BaseMixin, LoginView):
    template_name = 'account/login.html'


class CustomPasswordResetFromKeyView(BaseMixin, PasswordResetFromKeyView):
    template_name = 'account/password_reset_from_key.html'


class CustomPasswordResetFromKeyDoneView(BaseMixin, PasswordResetFromKeyDoneView):
    template_name = 'account/password_reset_from_key_done.html'


class CustomPasswordResetView(BaseMixin, PasswordResetView):
    template_name = 'account/password_reset.html'


class CustomSignupView(BaseMixin, SignupView):
    template_name = 'account/signup.html'
