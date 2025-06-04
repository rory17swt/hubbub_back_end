from rest_framework import serializers

from ..models import User


# Authentication
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def validate(self, data):
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError({ 'password': 'Your passwords do not match' })
        return data
    
    def create(self, validated_data):
        validated_data.pop('password_confirmation')
        return User.objects.create_user(**validated_data)
    
# This will be used when populating the owner on an event
class UsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']