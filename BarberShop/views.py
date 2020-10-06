from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from validate_docbr import CPF


# Status Procedure Payment Company Employee Client 
class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class ProcedureViewSet(viewsets.ModelViewSet):
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    #'client_id', 'company_fk', 'name', 'email', 'birthday', 
    #'dateJoined', 'doc', 'phone', 'cellphone', 'zipcode', 'adress', 
    #'number', 'complement', 'district', 'city', 'state', 'active', 'obs'
    def create(self, request, *args, **kwargs):
        cpf = CPF()
        client = Client()
        company = Company()
        try:
            company = Company.objects.get(company_id = 1)
            print(company.name)
            client = Client.objects.get(doc=request.data['doc'])
            return Response({'CPF Duplicado'})
        except:
                if str.isalpha(request.data['name']) == False:
                    return Response({'Nome invalido'})
                if(cpf.validate(request.data['doc'])):
                    client.company_fk = company
                    client.doc = request.data['doc']
                    client.name = request.data['name']
                    client.save()
                    return Response({'200 status created'})
                else:
                    return Response({'Invalido'})


class BugBountyViewSet(viewsets.ModelViewSet):
    #Pode se usar uma flag para controlar o method names e bloquear os methodos a minha escolha
    queryset = BugBounty.objects.all()
    serializer_class = BugBountySerializer
    http_method_names = ['get','post','head']

'''    def destroy(self, request, *args, **kwargs):
        return Response({'detail': request.method +' << NOT ALLOWEDs'})

    def update(self, request, *args, **kwargs):
        return Response({'detail': request.method +' << NOT ALLOWED'})

    def partial_update(self, request, *args, **kwargs):
        return Response({'detail': request.method +' << NOT ALLOWED'})'''