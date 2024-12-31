from rest_framework import serializers
from .models import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'username', 'email']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = Users.objects.create_user(**validated_data)
        return user