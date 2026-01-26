from rest_framework import serializers
from .models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    confirm = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'password', 'confirm', 'email']
        extra_kwargs = {
            'password': {'write_only': True}
        }   # password request qabul qiladi lekin respons qaytarmaydi
        
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm']:
            raise serializers.ValidationError({
                "message":"Password yoki confirm bir xil emas"
            })
        
        return attrs
    
    # def create(self, validated_data):
    #     validated_data.pop('confirm')
    #     password = validated_data.pop('password')
    #     user = User(**validated_data)
    #     user.set_password(password)
    #     user.save()
    #     return user 
    
    def create(self, validated_data):       #create_user():set_password() ni o‘zi qiladi
        validated_data.pop('confirm')
        user = User.objects.create_user(**validated_data)
        
        return user
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'role',
            'created_at',
        ]


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=150)
    
