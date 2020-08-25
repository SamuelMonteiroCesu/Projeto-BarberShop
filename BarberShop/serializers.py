from rest_framework import serializers
from .models import *


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['status_id', 'name','active']


class ProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedure
        fields = ['procedure_id', 'name','active','time','price']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['payment_id', 'name', 'active', 'discount','tax']

# Status Procedure Payment Company Employee Client
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['company_id', 'name', 'doc', 'zipcode', 'adress', 'number', 
        'complement', 'district', 'city', 'state', 'phone', 'cellphone', 'active']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['employee_id', 'company_fk', 'name', 'email', 'password', 'doc', 
        'phone', 'cellphone', 'active', 'obs']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['client_id', 'company_fk', 'name', 'email', 'birthday', 'dateJoined', 'doc', 
        'phone', 'cellphone', 'zipcode', 'adress', 'number', 'complement', 'district', 'city', 'state', 'active', 'obs']