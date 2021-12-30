from django.shortcuts import render, redirect
from Employee_Vacation.logic import vacation_logic
from Employee_Vacation.models import Employee
from django.http import HttpResponse
import json

def get_emp_id(request):
    return Employee.objects.filter(user=request.user).first()

def get_vacations(request):
    return render(request,'vacation/vacation_list.html')

def vacations_data(request):
    order = 'id'
    if request.GET.get('order[0][column]') == '0':
        order = 'description'
    elif request.GET.get('order[0][column]') == '1':
        order = 'from_date'
    elif request.GET.get('order[0][column]') == '2':
        order = 'to_date'
    elif request.GET.get('order[0][column]') == '3':
        order = 'duration'
    
    data = vacation_logic.vacations_data(get_emp_id(request), {
        'draw': int(request.GET.get('draw', 1)),
        'start': int(request.GET.get('start', 0)),
        'length': int(request.GET.get('length', 10)),
        'queryText': request.GET.get('search[value]', ''),
        'order': ('-' if request.GET.get('order[0][dir]')=='desc' else '')+order
    })

    return HttpResponse(json.dumps(data), content_type='application/json;charset=utf-8')

def get_vacation(request, vacation_id):
    vacation = vacation_logic.get_vacation(get_emp_id(request), vacation_id)
    return render(request, 'vacation/vacation_form.html', {
        "vacation":vacation, 
        "form_url":'edit_vacation' if vacation else 'add_vacation'
    })
    
def add_vacation(request):
    formData = request.POST
    data = {
        'employee': get_emp_id(request),
        'description': formData.get('description'),
        'from_date': formData.get('from_date'),
        'to_date': formData.get('to_date'),
        'duration': formData.get('duration')
        }
    vacation = vacation_logic.add_vacation(data)
    return redirect('vacations')
    
def update_vacation(request):
    formData = request.POST
    data = {
        'employee': get_emp_id(request),
        'vacation_id': formData.get('vacation_id'),
        'description': formData.get('description'),
        'from_date': formData.get('from_date'),
        'to_date': formData.get('to_date'),
        'duration': formData.get('duration')
    }
    res = vacation_logic.update_vacation(data)

    return redirect('vacations')


def delete_vacation(request,vacation_id):
    vacation_logic.delete_vacation(get_emp_id(request), vacation_id)
    return redirect('vacations')
