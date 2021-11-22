from django.shortcuts import render
from rest_framework   import generics 
from .serializer      import PersonaProfesionalSerializer
from .models          import PersonaProfesional
from django.db.models.query import QuerySet

class PersonaProfesionalListCreate(generics.ListCreateAPIView):
    queryset = PersonaProfesional.objects.all()

    serializer_class = PersonaProfesionalSerializer

class PersonaProfesionalUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = PersonaProfesional.objects.all()

    serializer_class = PersonaProfesionalSerializer

