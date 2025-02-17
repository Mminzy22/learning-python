from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()  # Custom user model
        fields = ["username", "email", "password1", "password2"]  # 필요한 필드
