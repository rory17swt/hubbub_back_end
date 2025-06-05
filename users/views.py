from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers.common import UserSerializer
from .serializers.populated import ProfileSerializer
from .serializers.tokens import CustomTokenSerializer


# Create your views here.
class SignUpView(APIView):
    def post(self, request):
        serialized_user = UserSerializer(data=request.data)
        serialized_user.is_valid(raise_exception=True)
        serialized_user.save()
        return Response({ f'detail': 'Sign up successful' })
    

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer


# Profile view
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile = ProfileSerializer(request.user)
        return Response(profile.data)
