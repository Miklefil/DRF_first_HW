from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        required = ['username', 'email', 'password']
        write_only_fields = ['password']