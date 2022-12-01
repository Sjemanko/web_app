from django.shortcuts import render
from .models import Product
from rest_framework.response import Response
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET'])
def product_list(request):
    if request.method == 'GET':
        product_data = Product.objects.all()
        serializer = ProductSerializer(product_data, many=True)
        return Response(serializer.data)