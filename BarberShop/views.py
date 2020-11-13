from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
from validate_docbr import CPF
import datetime
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

def home (request):
    return render(request, 'home.html')

# Status Procedure Payment Company Employee Client 
@permission_classes([IsAuthenticated])
class StatusViewSet(viewsets.ModelViewSet):
    print(IsAuthenticated)
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


@permission_classes([IsAuthenticated])
class ProcedureViewSet(viewsets.ModelViewSet):
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer

@permission_classes([IsAuthenticated])
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = AuthUser.objects.all()
    serializer_class = ClientSerializer
    def create(self, request, *args, **kwargs):
        #first_name, last_name, email, username, password, is_staff, is_active, is_superuser
        # name, birthday, doc, email, password
        user = User()
        print(IsAuthenticated)
        print(kwargs)
        try:
            user = User.objects.get(username = request.data['doc'])
        except:
            None
        print(user)
        if (user.username != ""):
            return Response({'400: DUPLICATED *DOCUMENT* - CHECK PLEASE'})
        user = User.objects.create_user(email = request.data['email'], first_name= request.data['name'],username=request.data['doc'], last_name=request.data['birthday'], password=request.data['birthday'], is_superuser=0, is_staff=0)
        user.save()
        return Response({'200: CLIENT CREATED --' +user.username })




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
@permission_classes([IsAuthenticated])
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