from rest_framework import serializers
from .models import Employee, Attendance

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"

    def validate(self, data):
        employee = data['employee']
        date = data['date']

        exists = Attendance.objects.filter(employee = employee, date = date).exists()

        if exists:
            raise serializers.ValidationError("Employee attendance marked for this date. Cant duplicate")
        
        return data
