from django.db.models import fields
from rest_framework import serializers
from .models        import PersonaProfesional

class PersonaProfesionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaProfesional
        fields = '__all__'

