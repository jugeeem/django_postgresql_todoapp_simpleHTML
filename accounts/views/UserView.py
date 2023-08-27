from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from accounts.models import Profile
from accounts.forms import UserCreationForm


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/login_signup.html'

    def form_valid(self, form):
        return super().form_valid(form)


class Login(LoginView):
    template_name = 'accounts/login_signup.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class AccountUpdateView(UpdateView):
    model = get_user_model()
    template_name = 'accounts/account.html'
    fields = ('username', 'email',)
    success_url = reverse_lazy('index')

    def get_object(self):
        # URL変数ではなく、現在のユーザーから直接pkを取得
        self.kwargs['pk'] = self.request.user.pk
        return super().get_object()


class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = 'accounts/profile.html'
    fields = ('name', 'zipcode', 'prefecture',
              'city', 'address1', 'address2', 'tel')
    success_url = reverse_lazy('profile')

    def get_object(self):
        # URL変数ではなく、現在のユーザーから直接pkを取得
        self.kwargs['pk'] = self.request.user.pk
        return super().get_object()
