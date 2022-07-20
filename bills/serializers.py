from datetime import datetime
from rest_framework import serializers

from bills.models import Bill


class BillSerializer(serializers.ModelSerializer):
    sum = serializers.FloatField()
    class Meta:
        model = Bill
        fields = "__all__"

    def validate(self, attrs):
        return attrs