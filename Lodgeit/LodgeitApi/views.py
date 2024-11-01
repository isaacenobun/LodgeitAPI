from django.shortcuts import render
from rest_framework import  viewsets

from .models import Staff, Company

from .serializers import StaffSerializer, CompanySerializer

# Create your views here.
class CompanyViewset(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class StaffViewset(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer