from django.shortcuts import render
from .models import Product
from rest_framework.response import Response
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


@api_view(['GET'])
def product_list(request):
    if request.method == 'GET':
        if request.query_params.get('product_name'):
            products_data = Product.objects.filter(product_name__contains=request.query_params.get('product_name'))
            serializer = ProductSerializer(products_data, many=True)
        else:
            product_data = Product.objects.all()
            serializer = ProductSerializer(product_data, many=True)
        return Response(serializer.data)
    


@api_view(['POST'])
def add_product(request):
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

@api_view(['PUT'])
def update_product(request, id):
    try:
        product = Product.objects.get(id=id)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


@api_view(['DELETE'])
def delete_product(request, id):
    try:
        product = Product.objects.get(id=id)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET'])
def show_male_products(request):
    if request.method == 'GET':
        products = Product.objects.filter(product_gender='ME')
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def show_female_products(request):
    if request.method == 'GET':
        products = Product.objects.filter(product_gender='FE')
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
