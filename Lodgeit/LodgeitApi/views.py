from django.shortcuts import render
from rest_framework import  viewsets

from .models import Staff,Company

from .serializers import StaffSerializer, CompanySerializer

from rest_framework.permissions import IsAuthenticated

# Create your views here.
class CompanyViewset(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
class StaffViewset(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    ordering_fields = ['id','email']
    ordering = ['id']
    search_fields = ['company__name']
    permission_classes = [IsAuthenticated]
    