from django.shortcuts import render

# Create your views here.

from rest_framework                 import generics 
from .serializer                    import PersonaClienteSerializer
from .models                        import PersonaCliente

class PersonaClienteListCreate(generics.ListCreateAPIView):
    queryset = PersonaCliente.objects.all()

    serializer_class = PersonaClienteSerializer

class PersonaClienteUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = PersonaCliente.objects.all()

    serializer_class = PersonaClienteSerializer