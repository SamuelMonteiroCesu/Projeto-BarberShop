from rest_framework import serializers
from .models import Status, Procedure


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['status_id', 'name','active']


class ProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedure
        fields = ['procedure_id', 'name','active','time','price']