from django.shortcuts           import render
from rest_framework             import generics, views, authentication, permissions, status 
from .serializer                import PersonaProfesionalSerializer, UserSerializer, UserCreationSerializer
from .models                    import PersonaProfesional
from rest_framework.response    import Response
from django.contrib.auth.models import User

class PersonaProfesionalListCreate(generics.ListCreateAPIView):
    queryset = PersonaProfesional.objects.all()

    serializer_class = PersonaProfesionalSerializer


class PersonaProfesionalUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = PersonaProfesional.objects.all()

    serializer_class = PersonaProfesionalSerializer


#Configs para recibir token - APIGateway
class UserRetrieve(views.APIView):

    # autenticacion por token
    authentication_classes = [authentication.TokenAuthentication]

    #la persona tiene que estar autenticada
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)   #request.user -> usuario de ese token
                                                    # lo serializamos con UserSerializer
        return Response(data=serializer.data, status=status.HTTP_200_OK)


# creamos User manual, para guardar info extra de profesioanl
class UserCreate(views.APIView):
    def post(self, request):
        #serializamos lo que llega en la peticion
        serializer = UserCreationSerializer(data=request.data)

        #validamos si es correcto(que no exista, contraseñas correctas,etc)
        if serializer.is_valid():
            #llamamos al ORM de User
            #con create_user creamos objetos manuales en la DB
            user = User.objects.create_user(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
            #creamos una persona soporte, y le enviamos el objeto con la info extra
            # en este caso solo utilizamos el campo extra edad
            PersonaProfesional.objects.create(user=user, tipoDocumento=request.data['tipoDocumento'], numeroDocumento=request.data['numeroDocumento'], perfil=request.data['perfil'])
            return Response(status=status.HTTP_201_CREATED)
