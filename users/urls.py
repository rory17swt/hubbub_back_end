from django.urls import path

from .views import SignUpView, ProfileView, CustomTokenObtainPairView


urlpatterns = [
    path('sign-up/', SignUpView.as_view()),
    path('sign-in/', CustomTokenObtainPairView.as_view()),
    path('profile/', ProfileView.as_view())
]