from django.urls import reverse_lazy  # URL 패턴을 문자열로 반환하는 유틸리티
from django.views.generic.edit import CreateView, UpdateView  # 제네릭 뷰: 생성(Create), 업데이트(Update)
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView  # 로그인, 로그아웃, 비밀번호 변경 뷰
from django.views.generic.detail import DetailView  # 제네릭 뷰: 상세 보기
from django.contrib.auth.mixins import LoginRequiredMixin  # 로그인을 요구하는 믹스인
from .forms import CustomUserForm, CustomPasswordChangeForm, ProfileUpdateForm  # 커스텀 폼 클래스들
from django.contrib.auth import get_user_model  # 현재 프로젝트에서 사용 중인 User 모델을 가져옴

from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, UpdateAPIView
    )
from .serializers import SignupSerializer, UserProfileSerializer, ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated
from .models import User
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password


# 모듈 수준 변수
# 현재 프로젝트에서 사용 중인 User 모델
User = get_user_model()


# 회원가입 API 뷰
class SignupAPIView(CreateAPIView):
    serializer_class = SignupSerializer
    queryset = User.objects.all()  # 전체 사용자 조회


# 회원 프로필 API 뷰
class ProfileAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]  # 로그인한 사용자만 접근 가능

    def get_object(self):
        # 현재 로그인한 사용자 반환
        return self.request.user


# 프로필 수정 API 뷰
class ProfileUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]  # 로그인한 사용자만 수정 가능

    def get_object(self):
        # 현재 로그인한 사용자 반환
        return self.request.user


# 비밀번호 변경 API 뷰
class ChangePasswordAPIView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]  # 로그인한 사용자만 접근 가능

    def update(self, request, *args, **kwargs):
        user = self.request.user
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            old_password = serializer.validated_data['old_password']
            new_password = serializer.validated_data['new_password']

            # 기존 비밀번호 확인
            if not check_password(old_password, user.password):
                return Response({"error": "현재 비밀번호가 올바르지 않습니다."}, status=400)

            # 새 비밀번호 설정
            user.set_password(new_password)
            user.save()

            return Response({"message": "비밀번호가 성공적으로 변경되었습니다."}, status=200)

        return Response(serializer.errors, status=400)


# 회원가입 뷰
class SignupView(CreateView):
    template_name = "accounts/signup.html"  # 사용할 템플릿 파일 경로
    form_class = CustomUserForm  # 회원가입 폼 클래스
    success_url = reverse_lazy('accounts:login')  # 회원가입 성공 시 로그인 페이지로 리다이렉트

# 로그인 뷰
class UserLoginView(LoginView):
    template_name = "accounts/login.html"  # 사용할 템플릿 파일 경로

# 로그아웃 뷰
class UserLogoutView(LogoutView):
    # LogoutView는 기본적으로 별도의 설정 없이 작동하므로 추가 코드 필요 없음
    pass

# 프로필 보기 뷰
class ProfileView(LoginRequiredMixin, DetailView):
    model = User  # User 모델을 사용
    template_name = "accounts/profile.html"  # 사용할 템플릿 파일 경로

    def get_object(self, queryset=None):
        # 현재 로그인한 사용자의 프로필 정보를 반환
        return self.request.user

# 프로필 수정 뷰
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User  # User 모델을 사용
    form_class = ProfileUpdateForm  # 프로필 수정 폼 클래스
    template_name = "accounts/profile_update.html"  # 사용할 템플릿 파일 경로
    success_url = reverse_lazy('accounts:profile')  # 수정 성공 시 프로필 페이지로 리다이렉트

    def get_object(self, queryset=None):
        # 현재 로그인한 사용자의 정보를 수정
        return self.request.user

# 비밀번호 변경 뷰
class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    form_class = CustomPasswordChangeForm  # 비밀번호 변경 폼 클래스
    template_name = "accounts/change_password.html"  # 사용할 템플릿 파일 경로
    success_url = reverse_lazy('accounts:profile')  # 변경 성공 시 프로필 페이지로 리다이렉트
