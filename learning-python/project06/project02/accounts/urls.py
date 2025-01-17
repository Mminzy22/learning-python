from django.urls import path
from .views import SignupView, UserLoginView, UserLogoutView, ProfileView, ProfileUpdateView, ChangePasswordView

app_name = "accounts"

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("profile-update/", ProfileUpdateView.as_view(), name="profile_update"),
    path("change-password/", ChangePasswordView.as_view(), name="change_password"),
]
