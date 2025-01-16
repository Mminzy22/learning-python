from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.detail import DetailView

from .forms import CustomUserForm


class SignupView(CreateView):
    # 템플릿 파일 경로
    template_name = "accounts/signup.html"
    form_class = CustomUserForm
    # 회원가입 성공 시 사용자를 리다이렉트할 URL
    success_url = reverse_lazy('accounts:login')


class UserLoginView(LoginView):
    pass


class UserLogoutView(LogoutView):
    pass


class ProfileView(DetailView):
    pass
