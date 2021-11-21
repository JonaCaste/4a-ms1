from django.db.models import fields
from rest_framework import serializers
from .models        import PersonaCliente
from django.contrib.auth.models import User

class PersonaClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaCliente
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']