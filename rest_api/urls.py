from django.urls import path, include
from rest_api.views import lista_personas, vista_persona_mod
from rest_api.viewsLogin import login


urlpatterns = [
    path('lista_personas/',lista_personas,name="lista_personas"),
    path('datos_personas/<id>',vista_persona_mod,name="modif_persona"),
    path('login/',login,name="login"),
]

