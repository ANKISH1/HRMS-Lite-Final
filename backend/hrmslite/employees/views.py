from django.shortcuts import render
from rest_framework import generics
from .models import Employee, Attendance
from .serializers import EmployeeSerializer, AttendanceSerializer
# Create your views here.


class EmployeeCreate(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDelete(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class AttendanceCreate(generics.CreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class AttendanceList(generics.ListAPIView):
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        employee_id = self.request.query_params.get('employee_id')
        if not employee_id:
            return Attendance.objects.none()
        return Attendance.objects.filter(employee_id = employee_id)