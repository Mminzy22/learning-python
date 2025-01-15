from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm  # 커스텀 폼 임포트


@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # 가입 후 자동 로그인
            return redirect("index")
    else:
        form = CustomUserCreationForm()
    context = {"form": form}
    return render(request, "accounts/signup.html", context)


@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)  # 인증 성공 시 로그인 처리
            return redirect("index")  # 로그인 후 리다이렉트
    else:
        form = AuthenticationForm()
    context = {"form": form}
    return render(request, "accounts/login.html", context)


@require_http_methods(["POST"])
def logout(request):
    auth_logout(request)  # 세션 정리
    return redirect("index")  # 로그아웃 후 메인 페이지로 리다이렉트


@require_http_methods(["GET"])
@login_required  # 로그인된 사용자만 접근 가능
def profile(request):
    return render(request, "accounts/profile.html", {"user": request.user})
