from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.views.generic import (CreateView, UpdateView)
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from ..models import Profile
from accounts.forms import UserCreationForm


class SignUpCreateView(CreateView):
    """Create signup"""
    form_class = UserCreationForm
    template_name = 'accounts/login_signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        return super().form_valid(form)


class Login(LoginView):
    """Show login form"""
    template_name = 'accounts/login_signup.html'

    def form_valid(self, form: AuthenticationForm) -> HttpResponse:
        """Security check complete. Log the user in."""
        return super().form_valid(form)

    def form_invalid(self, form: AuthenticationForm) -> HttpResponse:
        """Security check complete. Log the user in."""
        return super().form_invalid(form)


class AccountUpdateView(LoginRequiredMixin, UpdateView):
    """Update account"""
    model = get_user_model()
    template_name = 'accounts/account.html'
    fields = [
        'username',
        'email'
    ]
    success_url = reverse_lazy('account')

    def get_object(self):
        """Return the user record."""
        self.kwargs['pk'] = self.request.user.pk
        return super().get_object()


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """Update profile"""
    model = Profile
    template_name = 'accounts/profile.html'
    fields = [
        'name',
        'zipcode',
        'prefecture',
        'city',
        'address1',
        'address2',
        'tel'
    ]
    success_url = reverse_lazy('profile')

    def get_object(self):
        """Return the user record."""
        self.kwargs['pk'] = self.request.user.user.pk
        return super().get_object()
