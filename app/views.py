from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from .models import Personas
from .forms import PersonaForm, ContactoForm
from django.contrib import messages

# Create your views here.
def pagPrincipal(request):

    return render (request,'app/pagPrincipal.html')

def empMinero(request):

    return render (request,'app/empMinero.html')

def empAgropecuario(request):

    return render (request,'app/empAgropecuario.html')

def empRetail(request):

    return render (request,'app/empRetail.html')

def empInformaticos(request):

    return render (request,'app/empInformaticos.html')


def pagNosotros(request):

    return render (request,'app/pagNosotros.html')

def pagEmpleo(request):

    return render (request,'app/pagEmpleo.html')

#INICIO DE SESION PRUEBA

def pagIniciosesion(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        contra = request.POST['contra']
        try:
            persona = Personas.objects.get(correo_per=usuario)
        except Personas.DoesNotExist:
            messages.error(request, 'El usuario o la contraseña son incorrectos')
            return redirect('pagPrincipal')
        
        if check_password(contra, persona.clave_per):
            try:
                user = User.objects.get(username=persona.correo_per)
            except User.DoesNotExist:

                user = User.objects.create_user(username=persona.correo_per, password=contra)
            
        
            login(request, user)
            messages.success(request, '¡Registrado exitosamente!')
            return redirect('pagPrincipal')
        
        messages.error(request, 'El usuario o la contraseña son incorrectos')
        return redirect('iniciar')
    
    return render(request, 'app/pagIniciosesion.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('pagPrincipal')
        


            


#INGRESO RECLAMO

def pagReclamos(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto guardado"
        else:
            data["form"] = formulario

    return render(request, 'app/pagReclamos.html', data)


#REGISTRO USUARIO

def pagRegistro(request):
    datos = {
        'form': PersonaForm()
    }

    if request.method=='POST':
        formulario = PersonaForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']= "Guardado correctamente"

    return render(request, 'app/pagRegistro.html',datos)

#MODIFICAR USUARIO 

def pagModificar(request, id):
    auto = Personas.objects.get(id_per=id)
    datos = {
        'form': PersonaForm(instance=auto)
    }
    if request.method=='POST':
        formulario= PersonaForm(data=request.POST, instance=auto)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificado Correctamente"

    return render(request, 'app/pagModificar.html', datos)

#LISTAR USUARIO

def listar_E_persona(request):
    Personas = Personas.objects.all()
    datos = {
        "personas":Personas
    }
    return render(request, 'app/listar_E_persona.html',datos)

#BORRAR USUARIO

def form_D_persona(request, id):
    aut = Personas.objects.get(id=id)
    datos = {
        'form': PersonaForm(instance=aut)
    }
    if request.method=='POST':
        formulario= PersonaForm(data=request.POST, instance=aut)
        aut.delete()
        datos['mensaje'] = "Eliminado Correctamente"

    return render(request, 'app/form_D_persona.html', datos)




