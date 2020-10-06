from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from validate_docbr import CPF
import datetime


# Status Procedure Payment Company Employee Client 
class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    print(queryset.query)


class ProcedureViewSet(viewsets.ModelViewSet):
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer
    print(queryset.query)


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    print(queryset.query)

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    print(queryset.query)

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    print(queryset.query)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    print(queryset.query)

#'client_id', 'company_fk', 'name', 'email', 'birthday', 
#'dateJoined', 'doc', 'phone', 'cellphone', 'zipcode', 'adress', 
#'number', 'complement', 'district', 'city', 'state', 'active', 'obs'
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def create(self, request, *args, **kwargs):
        cpf = CPF()
        client = Client()
        company = Company()
        try:
            company = Company.objects.get(company_id = 1)
            client = Client.objects.get(doc=request.data['doc'])
            return Response({'400: DUPLICATED *DOC* - CHECK PLEASE'})
        except:
                
                if str.isalpha(request.data['name']) == False:
                    return Response({'400: INVALID *NAME* - CHECK PLEASE'})
                if(cpf.validate(request.data['doc'])):
                    client.company_fk = company
                    client.doc = request.data['doc']
                    client.name = request.data['name']
                    client.email = request.data['email']
                    client.birthday = request.data['birthday']
                    client.phone = request.data['phone']
                    client.cellphone = request.data['cellphone']
                    client.zipcode = request.data['zipcode']
                    client.adress = request.data['adress']
                    client.number = request.data['number']
                    client.district = request.data['district']
                    client.city = request.data['city']
                    client.state = request.data['state']
                    client.obs = request.data['obs']
                    client.save()
                    return Response({'200: CLIENT CREATED'})
                else:
                    return Response({'400: INVALID *DOC* - CHECK PLEASE'})


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
