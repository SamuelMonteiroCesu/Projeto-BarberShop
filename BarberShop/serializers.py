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

class BugBountySerializer(serializers.ModelSerializer):
    class Meta:
        http_method_name = ['POST','GET',]
        #'bug_id', 'name', 'content', 'solved'
        model = BugBounty
        fields = ['bug_id', 'name', 'subject', 'description']



class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ['id','first_name', 'last_name', 'email', 'username','password','is_staff']

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = "__all__"

#['client','professional','status','procedure','payment' ]
class AppointmentSerializer(serializers.ModelSerializer):
    #client = ClientSerializer(read_only=True)
    #professional = ClientSerializer(read_only=True)
    #status = StatusSerializer(read_only=True)
    #procedure = ProcedureSerializer(read_only=True)
    #payment = PaymentSerializer(read_only=True)
    class Meta:
        model = Appointment
        fields = "__all__"

class DayOffSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayOff
        fields = "__all__"