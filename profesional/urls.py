from django.urls    import path
from .views         import PersonaProfesionalListCreate, PersonaProfesionalUpdateDelete, UserRetrieve, UserCreate


urlpatterns = [
    path('persona-profesional/',            PersonaProfesionalListCreate.as_view()),
    path('persona-profesional/<pk>/',       PersonaProfesionalUpdateDelete.as_view()),

    # link para recibir token
    path('users/',                          UserRetrieve.as_view()),   

    # creamos User con info extra de profesional
    path('create-profesional/',             UserCreate.as_view()),
]

