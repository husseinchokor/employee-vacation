from django.shortcuts import render, redirect
from Employee_Vacation.logic import employee_logic

def check_login(request):
    if request.user.is_authenticated:
        return redirect('vacations')
    return redirect('loginpage')

def login(request):    
    return render(request, 'employee/login.html')

def logout(request):
    employee_logic.employee_logout(request)
    return redirect('loginpage')

def register(request):
    return render(request, 'employee/register.html')

def adduser(request):
    form = request.POST
    data = {
        'username': form.get('username'),
        'password': form.get('password'),
        'email': form.get('email'),
        'first_name': form.get('firstName'),
        'last_name': form.get('lastName'),
    }
    
    emp = employee_logic.adduser(data)
    
    return redirect('loginpage' if emp else 'register')

def check_user(request):
    formData = request.POST
    data = {
        'username': formData.get('username'),
        'password': formData.get('password'),
    }
    res = employee_logic.employee_login(request, data)
    return redirect('vacations' if res else 'loginpage')
