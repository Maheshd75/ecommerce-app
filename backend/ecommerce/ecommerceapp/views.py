from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Products
from .serializer import ProductsSerializer

# Create your views here.
@api_view(['GET','POST'])
def productsdata(request):
    if request.method == 'GET':
        items=Products.objects.get()
        serializer=ProductsSerializer(items,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        items=Products.objects.get()
        serializer=ProductsSerializer(request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

