from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from validate_docbr import CPF
import datetime
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

def home (request):
    return render(request, 'home.html')

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


class AuthUserViewSet(viewsets.ModelViewSet):
    queryset = AuthUser.objects.all()
    serializer_class = AuthUserSerializer

    def create(self, request, *args, **kwargs):
        #first_name, last_name, email, username, password, is_staff, is_active, is_superuser
        #name, birthday, doc, email
        request.data['name']
        user = User.objects.create_user(first_name= request.data['name'],username=request.data['doc'], last_name=request.data['birthday'], password=request.data['birthday'], is_superuser=1, is_staff=1)
        user.save()
        return Response({'200: CLIENT CREATED'})



'''
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
        except:
                if (client != None):
                    return Response({'400: DUPLICATED *DOCUMENT* - CHECK PLEASE'})
                if str.isalpha(request.data['name']) == False:
                    return Response({'400: INVALID *NAME* - CHECK PLEASE'})
                if(cpf.validate(request.data['doc'])):
                    client.company_fk = company
                    client.doc = request.data['doc']
                    client.name = request.data['name']
                    client.email = request.data['email']
                    #client.birthday = request.data['birthday']
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
'''

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