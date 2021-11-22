from django.db.models.query import QuerySet
from rest_framework     import generics
from rest_framework import serializers
from django.urls    import path
from .views         import PersonaClienteListCreate, PersonaClienteUpdateDelete

urlpatterns = [
    path('persona-cliente/',            PersonaClienteListCreate.as_view()),
    path('persona-cliente/<pk>/',    PersonaClienteUpdateDelete.as_view()),
]