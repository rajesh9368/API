from django.shortcuts import render
from rest_framework import viewsets
from .models import Company,Employee
from .serializers import CompanySerializer,EmployeeSerializer
from rest_framework.decorators import action
# Create your views here.
class  CompanyViewSet(viewsets.ModelViewSet):
  queryset = Company.objects.all()
  serializer_class = CompanySerializer
  # @action(detail=True,methods=['get'])
  # def employees(self,request,pk=None):
  # pass
class EmployeeViewSet(viewsets.ModelViewSet):
  queryset = Employee.objects.all()
  serializer_class = EmployeeSerializer