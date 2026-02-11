from django.shortcuts import render


def employees_page(request):
    return render(request, "employees/employees.html")

def attendance_page(request):
    return render(request, "employees/attendance.html")