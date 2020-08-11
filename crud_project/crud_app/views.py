from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.
def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("emp_list")
            except:
                pass
    else:
        form = EmployeeForm()

    return render(request,'crud_app/index.html',{'form':form})


def show(request):
    employees=Employee.objects.all()
    return render(request,"crud_app/show.html",{'employees':employees})



def destroy(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect("emp_list")


def edit(request, id):
    employee=Employee.objects.get(id=id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            try:
                # employee.ename = form.cleaned_data['ename']
                # employee.eemail = form.cleaned_data['eemail']
                # employee.econtact = form.cleaned_data['econtact']
                # employee.save()
                form.save()
        
                return redirect("emp_list")
            except:
                pass
    else:
        form = EmployeeForm()

    return render(request,'crud_app/edit.html',{'employee':employee})



def update(request,id):
    employee=Employee.objects.get(id=id)
    form=EmployeeForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request,'crus_app/edit.html',{'employee':employee})