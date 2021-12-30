from Employee_Vacation.models import Vacation, Employee
from django.db.models import Q 

def vacations_data(employee, data):
    filter = Q(employee=employee)
    if data.get('queryText'):
        filter &= Q(description__contains=data.get('queryText'))
    
    total = Vacation.objects.filter(filter).count()
    lst = Vacation.objects.filter(filter).order_by(data['order']).all()[data['start'] : (data['start']+1)*data['length']]

    return {
        "draw": data.get('draw'),
        "recordsTotal": total,
        "recordsFiltered": len(lst),
        "data": [{
                'id': x.id,
                'description': x.description,
                'from_date': x.from_date.strftime("%Y-%m-%d"),
                'to_date': x.to_date.strftime("%Y-%m-%d"),
                'duration': x.duration,
                'edit': 1,
                'del': 1
            } for x in lst]
    }

def get_vacation(employee, vacation_id):
    return Vacation.objects.filter(id = vacation_id, employee=employee).first()

def add_vacation(data):
    vacation = Vacation()
    vacation.employee = data['employee']
    vacation.description = data['description']
    vacation.from_date = data['from_date']
    vacation.to_date = data['to_date']
    vacation.duration = data['duration']
    vacation.save()
    
def update_vacation(data):
    vacation = get_vacation(data['employee'], data['vacation_id'])
    if vacation:
        vacation.description = data['description']
        vacation.from_date = data['from_date']
        vacation.to_date = data['to_date']
        vacation.duration = data['duration']
        vacation.save()
        
        return True if vacation else False
    
def delete_vacation(employee, vacation_id):
    return Vacation.objects.filter(id = vacation_id, employee=employee).delete()