from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

# CustomUserForm: 회원가입 폼
class CustomUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["username", "email", "bio", "password1", "password2"]

# PasswordChangeForm: 비밀번호 변경 폼
class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = get_user_model()
        fields = ["old_password", "new_password1", "new_password2"]

# ProfileUpdateForm: 프로필 수정 폼
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ["username", "email", "bio"]
