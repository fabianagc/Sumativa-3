from django.urls import path
from .views import pagPrincipal,pagIniciosesion,pagEmpleo,pagNosotros,pagRegistro,pagModificar,pagReclamos,empInformaticos,empRetail
urlpatterns = [
    path('', pagPrincipal, name="pagPrincipal"),
    path('emp-retail/', empRetail, name='empRetail'),
    path('pag-Iniciosesion/', pagIniciosesion, name='pagIniciosesion'),
    path('pag-nosotros/', pagNosotros, name='pagNosotros'),
    path('pag-registro/', pagRegistro, name="pagRegistro"),
    path('emp-informaticos/', empInformaticos, name="empInformaticos"),
    path('pag-empleo/', pagEmpleo, name="pagEmpleo"),
    path('pag-reclamos/', pagReclamos, name="pagReclamos"),
    path('pag-modificar/<id>',pagModificar , name="pagModificar"),
]
