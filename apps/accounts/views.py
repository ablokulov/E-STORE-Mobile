from django.contrib.auth import authenticate

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.views import  APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import UserRegisterSerializer, UserSerializer, UserLoginSerializer

class UserRegisterViews(CreateAPIView):
    
    serializer_class = UserRegisterSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = serializer.save()
        
        data = UserSerializer(user).data
        
        return Response(data,status=status.HTTP_201_CREATED)
    
class UserLoginViews(APIView):
    permission_classes = [AllowAny]
    
    def post(self,request:Request)->Response:
        serializer = UserLoginSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            data = serializer.data
            
            user = authenticate(username = data['username'], password = data['password'])
            
            if not user:
                return Response({
                    "detail": "Username yoki parol noto'g'ri"
                },status=status.HTTP_401_UNAUTHORIZED)
            
            if not user.is_active:
                return Response({
                    "detail":"Foydalanuvchi bloklangan" 
                },status=status.HTTP_403_FORBIDDEN)
 
            refresh = RefreshToken.for_user(user)
            
            data = {
                "User":UserSerializer(user).data,
                "tokens":{
                    "refresh_token": str(refresh),
                    "access_token" : str(refresh.access_token),
                }  
            }
            return Response(data,status=status.HTTP_201_CREATED)
        
        
class TokenRefreshViews(APIView):
    permission_classes = []
    
    def post(self,request:Request)->Response:
        refresh_token = request.data.get('refresh')
        
        if not refresh_token:
            pass
            