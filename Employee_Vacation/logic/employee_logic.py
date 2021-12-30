from Employee_Vacation.models import Employee
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def employee_login(request, data):
    user = User.objects.filter(username__iexact = data.get('username')).first()
    if user:
        auth = authenticate(username=data.get('username').lower(), password=data.get('password'))
        if auth:
            login(request, auth)
    return True if user and auth else False

def employee_logout(request):
    logout(request)

def adduser(employee):
    if User.objects.filter(email__iexact=employee.get('email')).count():
        return False
    
    if User.objects.filter(username__iexact=employee.get('username')).count():
        return False
    
    user = User()
    
    user.first_name = employee.get('first_name')
    user.last_name = employee.get('last_name')
    user.email = employee.get('email')
    user.username = employee.get('username')
    user.set_password(employee.get('password'))
    user.save()
    
    emp = Employee()
    emp.user = user
    emp.save()
    
    return emp