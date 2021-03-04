from django.urls import path
from .views import UserSignupView, UserProfileView

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name="signup"),
    path('profile/', UserProfileView.as_view(), name="profile"),
]
