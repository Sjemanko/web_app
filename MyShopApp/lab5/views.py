from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person, Team
from .serializers import PersonSerializer
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

@api_view(['GET', 'PUT', 'DELETE'])
def person_details(request, id):
    """
    Wyświetlenie modelu Osoba
    :param request:
    :param id: id osoby
    :return:
    """

    try:
        person = Person.objects.get(id=id)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        person_data = Person.objects.get(id=id)
        serializer = PersonSerializer(person_data)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def add_person(request):
    if request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(['GET'])
def person_list(request):
    """
    Lista wszystkich obiektów modelu Person.
    :param request:
    """
    if request.method == 'GET':
        if request.query_params.get('name'):
            persons_data = Person.objects.filter(first_name__contains=request.query_params.get('name'))
            serializer = PersonSerializer(persons_data, many=True)
        else:
            persons_data = Person.objects.all()
            serializer = PersonSerializer(persons_data, many=True)
        return Response(serializer.data)
