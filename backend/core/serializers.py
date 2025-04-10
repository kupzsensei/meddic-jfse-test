from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True , style={'input_type': 'password'})
    password_confirm = serializers.CharField(write_only=True , style={'input_type': 'password'})
    class Meta:
        model = User
        fields = ('username', 'password', 'password_confirm')

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError({'password_confirm': "Passwords do not match"})
        return data

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        validated_data.pop('password_confirm')
        return super().create(validated_data)
    
    