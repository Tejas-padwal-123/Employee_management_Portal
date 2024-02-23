from django.shortcuts import render, HttpResponse
from .models import Empployee, Role, Department
from datetime import datetime
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def all_emp(request):
    """
    This function will be resposiible fro representing data from db to frontend.
    here Empployee class is being accessed and all the vlaues stored in it well be fetched,
    then it will stored in form of dict format and then pass on to html template for representation purpose.
    In short well access table Employee fetch details fomat it and will pass to html to show on frontend.
    Autor:Tejas Padwal.

    """
    emps= Empployee.objects.all()
    print('emps: -', emps)
    context = {'emps' : emps}
    return render(request, 'view_all_emp.html', context)

def add_emp(request):
    """
    This function will conatin logic for storing data wich was passed from html temaplte file that need to be 
    updated/stored in database.
    Autor: Tejas Padwal.

    """
    print('request.method', request.method)
    if request.method == "POST":
        print('request.method is post')
        first_name = request.POST['first_name'] 
        last_name =  request.POST['last_name']
        department_id =  int(request.POST['department'])
        salary =  int(request.POST['salary'])
        bonuse =  int(request.POST['bonuse'])
        role_id =  int(request.POST['role'])
        phone =  int(request.POST['phone'])
        hire_date =  request.POST['hire_date']
        role_instance  = Role.objects.get(id=role_id)
        print('role_instance', role_instance)
        #department_instance = Department.objetcs.get(id=department_id)
        department_instance = Department.objects.get(id=department_id)
        print('department_instance',department_instance )

        new_emp = Empployee(first_name=first_name, last_name=last_name, dept=department_instance, salary=salary,
                  bonuse=bonuse, role=role_instance, phone=phone, hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("Employeee added succesfully.")
    elif request.method == 'GET':
        print('request.method is not post')
        return render(request, 'add_emp.html')
    else:
        return HttpResponse("An Exception has been occursss...")

def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            #this will fetch employee details from table on basis of employee id(which is being get passed on from html,urls)
            emp_to_remove = Empployee.objects.get(id=emp_id)
            #employee will get deleted by using this 
            emp_to_remove.delete()                       
            return HttpResponse("Employee deleted Successfully.")
        except:
            return HttpResponse("failed to delete Employee.")
    # we are fetingg all the information from employee table and then sleective information will be shown
    # from dorpdown like(firstname lastname) on basis of wich we will fetch it's id and then again pass that id
    # to this function again.
    emps= Empployee.objects.all()
    print('emps: -', emps)
    context = {'emps' : emps}
    return render(request, 'remove_emp.html', context)


def filter_emp(request):
    if request.method =='POST':
        name = request.POST['name'] 
        department = request.POST['department']
        role = request.POST['role']
        emps= Empployee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name)| Q(last_name__icontains = name))
        if department:
            emps = emps.filter(department_name = deparment)
        if role:
            emps = emps.filter(role_name = role)
        context ={'emps':emps}
        return render(request, 'view_all_emp.html', context)
    elif request.method =='GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse("faild to filter details for Employee.")

