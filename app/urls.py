from django.urls import path
from .views import pagPrincipal,pagIniciosesion,pagEmpleo,pagNosotros,pagRegistro,pagModificar,pagReclamos,empInformaticos,empRetail,empAgropecuario,empMinero
urlpatterns = [
    path('', pagPrincipal, name="pagPrincipal"),
    path('emp-retail/', empRetail, name='empRetail'),
    path('pag-Iniciosesion/', pagIniciosesion, name='pagIniciosesion'),
    path('pag-nosotros/', pagNosotros, name='pagNosotros'),
    path('pag-registro/', pagRegistro, name="pagRegistro"),
    path('emp-informaticos/', empInformaticos, name="empInformaticos"),
    path('emp-agropecuario/', empAgropecuario, name="empAgropecuario"),
    path('emp-minero/', empMinero, name="empMinero"),
    path('pag-empleo/', pagEmpleo, name="pagEmpleo"),
    path('pag-reclamos/', pagReclamos, name="pagReclamos"),
    path('pag-modificar/<id>',pagModificar , name="pagModificar"),
]
