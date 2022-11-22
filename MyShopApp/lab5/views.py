from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person, Team
from .serializers import PersonSerializer, TeamSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authtoken.models import Token

# Create your views here.
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def person_details(request, id):
    """
    GET, PUT, DELETE on Person (details)
    :param request:
    :param id: id osoby
    :return:
    """
    is_tokened = Token.objects.filter(user=request.user)
    try:
        person = Person.objects.get(id=id)
        if request.user != person.owner:
            return Response({ "detail": "Nie podano danych uwierzytelniających."})
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        if is_tokened:
            serializer = PersonSerializer(person)
            return Response(serializer.data)
        else:
            return Response({"message": "brak token"})

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
    """
    Add person function
    :param request:
    :return:
    """
    if request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(['GET'])
def person_list(request):
    """
    List of all persons
    :param request:
    """
    if request.method == 'GET':
        if request.query_params.get('first_name'):
            persons_data = Person.objects.filter(first_name__contains=request.query_params.get('first_name'))
            serializer = PersonSerializer(persons_data, many=True)
        else:
            persons_data = Person.objects.all()
            serializer = PersonSerializer(persons_data, many=True)
        return Response(serializer.data)
    


@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def update_person(request, pk):
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_person(request, pk):
    try:
        person = Person.objects.get(pk=pk)
        is_tokened = Token.objects.filter(user=request.user)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    serializer = PersonSerializer(person, data=request.data)
    if request.method == 'DELETE': 
        if is_tokened:
            person.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message": "Brak tokenu uwierzytelniającego"})    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET', 'PUT', 'DELETE'])
def team_details(request, id):
    """
    GET, PUT, DELETE on team (details)
    :param request:
    :param id:
    :return:
    """

    try:
        team = Team.objects.get(id=id)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        team_data = Team.objects.get(id=id)
        serializer = TeamSerializer(team_data)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = TeamSerializer(team, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def add_team(request):
    """
    Add team function
    :param request:
    :return:
    """

    if request.method == 'POST':
        serializer = TeamSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(['GET'])
def team_list(request):
    """
        List of all teams
        :param request:
    """
    if request.method == 'GET':
        persons_data = Team.objects.all()
        serializer = TeamSerializer(persons_data, many=True)
        return Response(serializer.data)


@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def show_team_members(request, id):
    is_tokened = Token.objects.filter(user=request.user)
    try:
       persons_data = Person.objects.filter(team=id)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        if is_tokened:
            serializer = PersonSerializer(persons_data, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "Brak tokenu uwierzytelniającego"})  