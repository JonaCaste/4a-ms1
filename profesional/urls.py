from django.urls    import path
from .views         import PersonaProfesionalListCreate, PersonaProfesionalUpdateDelete


urlpatterns = [
    path('persona-profesional/',            PersonaProfesionalListCreate.as_view()),
    path('persona-profesional/<pk>',    PersonaProfesionalUpdateDelete.as_view()),
]

