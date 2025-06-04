from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import SignUpView, ProfileView


urlpatterns = [
    path('sign-up/', SignUpView.as_view()),
    path('sign-in/', TokenObtainPairView.as_view()),
    path('profile/', ProfileView.as_view())
]