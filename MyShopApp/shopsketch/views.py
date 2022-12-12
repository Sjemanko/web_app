from django.shortcuts import render
from .models import Product, ShoppingCart, OrderedItems
from rest_framework.response import Response
from .serializers import ProductSerializer, ShoppingCartSerializer, OrderedItemsSerializer, CartItemsSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.contrib.auth.models import User
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


@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def create_shopping_cart(request):
    if isinstance(request.user, User):
        ShoppingCart.objects.create(
            owner = request.user
        )
        content = {   
            'user': str(request.user),  
            'status': 'Shopping cart has been created successfully'
        }
    else:
        content = {
            'status': 'Shopping cart hasn\'t been created. Create account to make a shopping cart.'
        }
    return Response(content)


@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def show(request):
    qs = OrderedItems.objects.all()
    serializer = OrderedItemsSerializer(qs, many=True)
    return Response(serializer.data)


@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def show_my_orders(request):
    if (isinstance(request.user, User)) and request.method == 'GET':
        user_orders = OrderedItems.objects.filter(shopping_cart__owner__username=request.user)
        serializer = CartItemsSerializer(user_orders, many=True)
        return Response(serializer.data)
    else:
        content={'status': 'Log In to show cart.'}
        return Response(content)


@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def create_order(request):
    if (isinstance(request.user, User)) and request.method == 'POST':
        order_serializer = OrderedItemsSerializer(data=request.data)
        order_serializer.is_valid(raise_exception=True)
        order_serializer.save()
        return Response(order_serializer.data)
    else:
        content={'status': 'Log In to show cart.'}
        return Response(content)
    # if request.method == 'POST':
    #     serializer = ProductSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)


@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def remove_order(request, pk):
    pass


@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['PUT'])
def update_order(request, pk):
    pass


@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def show_order(request, pk):
    pass


@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['PUT'])
def confirm_order(request, pk):
    pass

