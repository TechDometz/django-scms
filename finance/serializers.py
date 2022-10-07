from rest_framework import serializers

from .models import *
from sis.serializers import StudentSerializer
from users.serializers import AccountantSerializer

class AllocationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Allocation
        fields = "__all__"

class PaymentAllocationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PaymentAllocation
        fields = "__all__"

class ReceiptSerializer(serializers.ModelSerializer):
    student = serializers.SerializerMethodField(read_only=True)
    paid_for = serializers.SerializerMethodField(read_only=True)
    received_by = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Receipt
        fields = ('id', 'student', 'paid_for', 'received_by', 'date', 'payer', 'amount', 'receipt_no')
    
    def get_student(self, obj):
        student = obj.student
        serializer = StudentSerializer(student, many=False)
        student = serializer.data['first_name'] + " " + serializer.data['last_name']
        return student
    
    def get_paid_for(self, obj):
        paid_for = obj.paid_for
        serializer = AllocationSerializer(paid_for, many=False)
        paid_for = serializer.data['name']
        return paid_for

    def get_received_by(self, obj):
        received_by = obj.received_by
        serializer = AccountantSerializer(received_by, many=False)
        received_by = serializer.data['user']

        return received_by

class PaymentSerializer(serializers.ModelSerializer):
    paid_for = serializers.SerializerMethodField(read_only=True)
    paid_by = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Payment
        fields = "__all__"
    
    def get_paid_for(self, obj):
        paid_for = obj.paid_for
        serializer = PaymentAllocationSerializer(paid_for, many=False)
        paid_for = serializer.data['name']
        return paid_for

    def get_paid_by(self, obj):
        paid_by = obj.paid_by
        serializer = AccountantSerializer(paid_by, many=False)
        paid_by = serializer.data['user']

        return paid_by


