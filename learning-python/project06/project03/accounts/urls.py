from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    )
from .views import (
    SignupAPIView,
    ProfileAPIView,
    ProfileUpdateAPIView,
    ChangePasswordAPIView,

    SignupView, 
    UserLoginView, 
    UserLogoutView, 
    ProfileView, 
    ProfileUpdateView, 
    ChangePasswordView,
    )


app_name = "accounts"

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("profile-update/", ProfileUpdateView.as_view(), name="profile_update"),
    path("change-password/", ChangePasswordView.as_view(), name="change_password"),
]

urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/signup/', SignupAPIView.as_view(), name='api_signup'),
    path('api/profile/', ProfileAPIView.as_view(), name='api_profile'),
    path('api/profile/update/', ProfileUpdateAPIView.as_view(), name='api_profile_update'),
    path('api/change-password/', ChangePasswordAPIView.as_view(), name='api_change_password'),
]

