from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.models import Product
from api.serializers import UserSerializer, GroupSerializer, ProductSerializer
from django.shortcuts import get_object_or_404 
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer 

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def retrieve(self, request, pk=None):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(product)
        return Response({'results':serializer.data}) 