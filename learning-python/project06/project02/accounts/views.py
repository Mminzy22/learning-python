from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CustomUserForm, CustomPasswordChangeForm, ProfileUpdateForm
from django.contrib.auth import get_user_model

User = get_user_model()


class SignupView(CreateView):
    template_name = "accounts/signup.html"
    form_class = CustomUserForm
    success_url = reverse_lazy('accounts:login')


class UserLoginView(LoginView):
    template_name = "accounts/login.html"


class UserLogoutView(LogoutView):
    pass


class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "accounts/profile.html"

    # 현재 로그인한 사용자의 프로필 정보를 보여줌
    def get_object(self, queryset=None):
        return self.request.user


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileUpdateForm
    template_name = "accounts/profile_update.html"
    success_url = reverse_lazy('accounts:profile')

    # 현재 로그인한 사용자의 정보를 수정
    def get_object(self, queryset=None):
        return self.request.user


class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = "accounts/change_password.html"
    success_url = reverse_lazy('accounts:profile')
