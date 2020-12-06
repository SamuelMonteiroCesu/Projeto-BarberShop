from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
from validate_docbr import CPF
import datetime
from rest_framework import status
import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from .utility import *
import random
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.viewsets import ReadOnlyModelViewSet


class ActionBasedPermission(AllowAny):
    """
    Grant or deny access to a view, based on a mapping in view.action_permissions
    """
    def has_permission(self, request, view):
        for klass, actions in getattr(view, 'action_permissions', {}).items():
            if view.action in actions:
                return klass().has_permission(request, view)
        return False



def home (request):
    return render(request, 'home.html')

@api_view(['POST',])
def PassRecoverViewSet(request):
    try:
        user = User.objects.get(username = request.data['CPF'],email = request.data['email'],is_staff = True)
    except:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    x = str(random.randint(10000000,99999999))
    user.password = x
    user.set_password(user.password)
    subject = "BARBEARIA EBENEZER | RECUPERAÇÃO DE SENHA!"
    content = "Sua nova senha é: "+x
    u = Emails().sendmails(user.email,subject,content)
    user.save()
    return Response("Senha enviada para o seu Email")


@api_view(['GET',])
@permission_classes([IsAuthenticated])
def GetUserViewSet(request):
    try:
        user = User.objects.get(id = request.user.id)
    except:
        return Response(status = status.HTTP_404_NOT_FOUND)
    serializer = ClientSerializer(user)
    return Response(serializer.data)


@api_view(['GET',])
@permission_classes([IsAuthenticated])
def GetProfViewSet(request):
    try:
        user = User.objects.filter(is_staff = True).filter(is_active=True)
    except:
        return Response(status = status.HTTP_404_NOT_FOUND)
    serializer = ClientSerializer(user, many = True)
    return Response(serializer.data)


@api_view(['POST',])
@permission_classes([IsAuthenticated])
def PassChangeViewSet(request):
    try:
        user = User.objects.get(id = request.user.id)
    except:
        return Response(status = status.HTTP_404_NOT_FOUND)
    user.password = request.data['newpassword']
    user.set_password(user.password)
    user.save()
    return Response("Senha alterada com sucesso")


@api_view(['GET','POST',])
@permission_classes([IsAuthenticated])
def FreescheduleViewSet(request):
    print('------------------------')
    print(request.data)
    print('------------------------')
    free = []
    weekday = Time().convertweekday(request.data['date'])
    dayoff = []
    try:
        dayoff = DayOff.objects.filter(daydate = request.data['date']).filter(professional=request.data['professional'])
        schedule = Schedule.objects.filter(professional=request.data['professional']).filter(weekday=weekday)
        busy = Appointment.objects.filter(professional=request.data['professional']).filter(appdate = request.data['date'])

    except:
        pass
    if len(dayoff) >= 1 and request.user.is_staff == False:
        print('---------------'+request.user.username)
        for i in dayoff:
            return Response(i.reason)
        
    busy = list(busy)
    busyclient = []
    for i in schedule:
        free += Time().FreeSchedule(i,busy)
    for i in free:
        app = Appointment()
        app.apphour = i
        app.appdate = request.data['date']
        busyclient.append(app)
    busy += busyclient
    busy = sorted(busy,key = lambda x: x.apphour)
    busy = AppointmentSerializer(busy,many = True)
    if request.user.is_staff:
        return Response(busy.data)
    else:
        busyclient = AppointmentSerializer(busyclient,many = True)
        return Response(busyclient.data)



@api_view(['GET','POST',])
@permission_classes([IsAuthenticated])
def MyScheduleViewSet(request):
    print('------------------------')
    print(request.data)
    print('------------------------')
    free = []
    weekday = Time().convertweekday(request.data['date'])
    dayoff = []
    try:
        dayoff = DayOff.objects.filter(daydate = request.data['date']).filter(professional=request.user.id)
        schedule = Schedule.objects.filter(professional=request.user.id).filter(weekday=weekday)
        busy = Appointment.objects.filter(professional=request.user.id).filter(appdate = request.data['date'])

    except:
        pass
    if len(dayoff) >= 1 and request.user.is_staff == False:
        print('---------------'+request.user.username)
        for i in dayoff:
            return Response(i.reason)
        
    busy = list(busy)
    busyclient = []
    for i in schedule:
        free += Time().FreeSchedule(i,busy)
    for i in free:
        app = Appointment()
        app.apphour = i
        app.appdate = request.data['date']
        busyclient.append(app)
    busy += busyclient
    busy = sorted(busy,key = lambda x: x.apphour)
    busy = AppointmentSerializer(busy,many = True)
    print("---------------")
    print(request.user.username)
    print(request.user.is_staff)
    print("---------------")
    return Response(busy.data)


# Status Procedure Payment Company Employee Client 
#@permission_classes([IsAuthenticated])
class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = (IsAdminUser,)

'''
    def list(self, request):
        data = {}
        data['user'] = []
        data['user'].append(request.user.first_name)
        data['user'].append(request.user.id)
        queryset = Status.objects.all()
        serializer = StatusSerializer(queryset,many=True)
        data['data'] = serializer.data
        print("---------------")
        print(data)
        usuario = User.objects.get(id = request.user.id)
        print(usuario)
        print("---------------")
        return Response(data)
'''


@permission_classes([IsAuthenticated])
class ProcedureViewSet(viewsets.ModelViewSet):
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer

    permission_classes = (ActionBasedPermission,)
    action_permissions = {
        #IsAuthenticated: ['update', 'partial_update', 'destroy', 'list', 'create'],
        IsAdminUser: ['update', 'partial_update', 'destroy', 'list', 'create','retrieve'],
        AllowAny: []
    }

@permission_classes([IsAuthenticated])
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    permission_classes = (ActionBasedPermission,)
    action_permissions = {
        #IsAuthenticated: ['update', 'partial_update', 'destroy', 'list', 'create'],
        IsAdminUser: ['update', 'partial_update', 'destroy', 'list', 'create','retrieve'],
        AllowAny: []
    }
    


class ClientViewSet(viewsets.ModelViewSet):
    queryset = AuthUser.objects.all()
    serializer_class = ClientSerializer

    permission_classes = (ActionBasedPermission,)
    action_permissions = {
        #IsAuthenticated: ['update', 'partial_update', 'destroy', 'list', 'create'],
        IsAdminUser: ['update', 'partial_update', 'destroy', 'list', 'create','retrieve'],
        AllowAny: ['create',]
    }



    def create(self, request, *args, **kwargs):
        #first_name, last_name, email, username, password, is_staff, is_active, is_superuser
        # name, birthday, doc, email, password
        user = User()
        try:
            user = User.objects.get(username = request.data['username'])
        except:
            None
        if (user.username != ""):
            return Response(status = status.HTTP_404_NOT_FOUND)
            
        if(request.user.is_staff == True):
            request.data['is_staff'] = bool(request.data['is_staff'])
            print(request.data['is_staff'])
            user = User.objects.create_user(email = request.data['email'], first_name= request.data['first_name'],username=request.data['username'], last_name=request.data['last_name'], password=request.data['last_name'], is_superuser=0, is_staff=request.data['is_staff'])        
            user.save()
            serializer = ClientSerializer(user)
            return Response(serializer.data)
        
        user = User.objects.create_user(email = request.data['email'], first_name= request.data['first_name'],username=request.data['username'], last_name=request.data['last_name'], password=request.data['last_name'], is_superuser=0, is_staff=0)
        user.save()
        serializer = ClientSerializer(user)
        return Response(serializer.data)






@permission_classes([IsAuthenticated])
class BugBountyViewSet(viewsets.ModelViewSet):
    #Pode se usar uma flag para controlar o method names e bloquear os methodos a minha escolha
    queryset = BugBounty.objects.all()
    serializer_class = BugBountySerializer
    http_method_names = ['get','post','head']




class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    
    permission_classes = (ActionBasedPermission,)
    action_permissions = {
        IsAuthenticated: ['create','list','retrieve'],
        IsAdminUser: ['update', 'partial_update', 'destroy', 'list', 'create','retrieve'],
    }

    def destroy(self, request, pk=None):
        instance = Appointment.objects.get(pk =pk)
        instance.active = False
        instance.save()
        serializers = AppointmentSerializer(instance)
        return Response(serializers.data)


    def retrieve(self, request, pk=None):
        instance = Appointment.objects.get(pk =pk)
        if (request.user.is_staff == False) and (instance.client.id != request.user.id):
            return Response(status = status.HTTP_404_NOT_FOUND)        
        serializers = AppointmentSerializer(instance)
        return Response(serializers.data)


    def list(self, request):
        print(request.user.username)
        if request.user.is_staff:
            queryset = queryset = Appointment.objects.all()
        else:
            queryset = queryset = Appointment.objects.filter(client = request.user.id)
        queryset = sorted(queryset,key = lambda x: (x.appdate[6:10],x.appdate[3:5],x.appdate[0:2],x.apphour))
        serializer = AppointmentSerializer(queryset,many=True)
        return Response(serializer.data)




class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = (IsAdminUser,)

class DayOffViewSet(viewsets.ModelViewSet):
    queryset = DayOff.objects.all()
    serializer_class = DayOffSerializer
    permission_classes = (IsAdminUser,)
    