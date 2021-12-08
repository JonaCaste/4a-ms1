from django.db.models import fields
from rest_framework import serializers
from .models        import PersonaProfesional
from django.contrib.auth.models import User


class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PersonaProfesionalSerializer(serializers.ModelSerializer):

    class Meta:
        model = PersonaProfesional
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    #sobreescribimos profesional
    profesional = PersonaProfesionalSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profesional']

