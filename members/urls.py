from django.urls import path
from .views import UserSignupView, UserProfileView, PasswordChangeView, ShowProfilePageView, EditProfilePageView, CreateProfilePageView

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name="signup"),
    path('profile/', UserProfileView.as_view(), name="profile"),
    path('password/', PasswordChangeView.as_view(template_name='registration/change-password.html')),
    path('<int:pk>/profile', ShowProfilePageView.as_view(), name='show_profile_page'),
    path('<int:pk>/edit_profile', EditProfilePageView.as_view(), name='edit_profile'),
    path('create_profile', CreateProfilePageView.as_view(), name='create_profile'),
]
