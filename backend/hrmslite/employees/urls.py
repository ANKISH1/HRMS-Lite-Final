from django.urls import path
from .views import EmployeeCreate, EmployeeDelete, AttendanceCreate, AttendanceList
from .views_ui import employees_page, attendance_page

urlpatterns = [
    path('api/employees/', EmployeeCreate.as_view()),
    path('api/employees/<int:pk>/', EmployeeDelete.as_view()),
    path('api/attendance/', AttendanceCreate.as_view()),
    path('api/attendance/list/', AttendanceList.as_view()),

    path('employees-ui/', employees_page),
    path('attendance-ui/', attendance_page)


]