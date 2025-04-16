from rest_framework import serializers
from .models import Company,Employee
class CompanySerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    company_id = serializers.ReadOnlyField()
    model=Company
    fields = ['company_id','name','location','about','type','added_date','active']
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
  id=serializers.ReadOnlyField()
  class Meta:
    model=Employee
    fields = "__all__"