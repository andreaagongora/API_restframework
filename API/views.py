from django.shortcuts import render
from rest_framework import generics
from .models import Api
from .serializers import ApiSerializer

# Create your views here.
class ApiList(generics.ListCreateAPIView):
    queryset = Api.objects.all()
    serializer_class = ApiSerializer

class ApiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Api
    serializer_class = ApiSerializer