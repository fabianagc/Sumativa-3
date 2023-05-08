from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from app.models import Personas
from .serializers import PersonaSerializers
from .serializers import PersonaSerializers2

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_personas(request):
    if request.method == 'GET':
        persona = Personas.objects.all()
        serializer = PersonaSerializers(persona,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PersonaSerializers(data = data)
        if serializer.is_valid():
           serializer.save()
           return  Response(serializer.data,status= status.HTTP_201_CREATED)
        else:
            return  Response(serializer.error,status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def vista_persona_mod(request, id):
    try:
        p = Personas.objects.get(id_per=id)
    except Personas.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PersonaSerializers2(p)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PersonaSerializers2(p, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        p.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        
    
    
