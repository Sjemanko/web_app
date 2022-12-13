from django.shortcuts import render
from .models import Product, ShoppingCart, OrderedItems
from rest_framework.response import Response
from .serializers import ProductSerializer, ShoppingCartSerializer, OrderedItemsSerializer, CartItemsSerializer, OrderSerializer
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


@api_view(['POST'])
def create_order(request):
    order_serializer = OrderSerializer(data=request.data)
    order_serializer.is_valid(raise_exception=True)
    order_serializer.save()
    return Response(order_serializer.data)


#########
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def remove_order(request, id):
    try:
        order = OrderedItems.objects.get(id=id)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#########

@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['PUT'])
def update_order(request, id):
    try:
        order = OrderedItems.objects.get(id=id)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if (isinstance(request.user, User)) and request.method == 'PUT':
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        content={'status': 'Log In to update cart.'}
        return Response(content)


@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def show_order(request, id):
    if (isinstance(request.user, User)) and request.method == 'GET':
        orders = OrderedItems.objects.get(id=id)
        serializer = CartItemsSerializer(orders)
        return Response(serializer.data)
    else:
        content={'status': 'Log In to show order.'}
        return Response(content)


@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def confirm_order(request, id):
    if (isinstance(request.user, User)) and request.method == 'GET':
        status = ShoppingCart.objects.get(id=id)
        serializer = ShoppingCartSerializer(status, data={"ordered": True})
        serializer.is_valid()
        serializer.save()
        content={'status': 'Order has been updated.'}
        return Response(content)
    else:
        content={'status': 'Log In to update order status.'}
        return Response(content)


@api_view(['GET'])
def get_cart(request, id):
    qs = ShoppingCart.objects.get(id=id)
    qs.total_price = count_total_sum(request, id=id)
    serializer = ShoppingCartSerializer(qs)
    return Response(serializer.data)

@api_view(['GET'])
def get_carts(request):
    qs = ShoppingCart.objects.all()
    print(qs)
    for i in range(len(qs)):
        qs[i].total_price = count_total_sum(request, id=qs[i].id)
    serializer = ShoppingCartSerializer(qs, many=True)
    return Response(serializer.data)


def count_total_sum(request, id):
    user_orders = OrderedItems.objects.filter(shopping_cart__id=id)
    cost_of_ordered_items = []
    for i in range(0,len(user_orders)):
        cost_of_ordered_items.append(user_orders[i].quantity * user_orders[i].product.product_price)
    print(cost_of_ordered_items)
    print(sum(cost_of_ordered_items))
    return sum(cost_of_ordered_items)
