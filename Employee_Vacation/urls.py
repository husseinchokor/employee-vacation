"""Employee_Vacation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Employee_Vacation.views import vacation
from Employee_Vacation.views import employee
from ctypes.test.test_pickling import name

urlpatterns = [
    path('', employee.check_login, name='check_login'),
    path('admin/', admin.site.urls),
    path('vac/list',vacation.get_vacations,name = 'vacations'),
    path('vac/data',vacation.vacations_data,name = 'vacations_data'),
    path('vac/add', vacation.add_vacation, name='add_vacation'),
    path('vac/get/<int:vacation_id>', vacation.get_vacation, name='get_vacation'),
    path('vac/edit', vacation.update_vacation, name='edit_vacation'),
    path('vac/delete/<int:vacation_id>', vacation.delete_vacation, name='delete_vacation'),
    path("login/",employee.login,name = 'loginpage' ),
    path("check_login/", employee.check_user, name = 'login' ),
    path("logout/", employee.logout, name = 'logout' ),
    path("register/", employee.register, name = 'register' ),
    path("adduser/", employee.adduser, name = 'adduser' )

]
