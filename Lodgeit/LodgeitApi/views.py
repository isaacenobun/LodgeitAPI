from django.shortcuts import render
from rest_framework import  viewsets

from django.contrib.auth import get_user_model
Staff = get_user_model()

from .serializers import StaffSerializer

# Create your views here.
class StaffViewset(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer