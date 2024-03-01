from django.shortcuts import render,redirect
from .models import Department,EmployDetails
from django.db.models import Q

# Create your views here.
def create(request):
    data=Department.objects.all()
    if request.method=="POST":
        employ_name=request.POST.get('employ_name')
        employ_number=request.POST.get('employ_number')
        employ_department=Department.objects.get(department_id=request.POST.get('employ_department'))

        employ_obj=EmployDetails()
        employ_obj.employ_name=employ_name
        employ_obj.employ_number=employ_number
        employ_obj.employ_department=employ_department

        employ_obj.save()
        return redirect(show)
    return render(request,'create.html',{'value':data})

def show(request):
    data=EmployDetails.objects.all()
    if request.method=="POST":
        search=request.POST.get('search')
        data=EmployDetails.objects.filter(Q(employ_name__icontains=search) | Q(employ_department__department_name__icontains=search) | Q(employ_number__icontains=search))
        return render(request,'show.html',{'value':data})


    return render(request,'show.html',{'value':data})

def delete(request,id):
    data=EmployDetails.objects.filter(id=id)
    data.delete()
    return redirect(show)

def update(request,id):
    data=EmployDetails.objects.filter(id=id)
    data2=Department.objects.all()
    if request.method=="POST":
        remove=EmployDetails.objects.filter(id=id)
        remove.delete()
        employ_name=request.POST.get('employ_name')
        employ_number=request.POST.get('employ_number')
        employ_department=Department.objects.get(department_id=request.POST.get('employ_department'))

        employ_obj=EmployDetails()
        employ_obj.employ_name=employ_name
        employ_obj.employ_number=employ_number
        employ_obj.employ_department=employ_department

        employ_obj.save()
        return redirect(show)
    return render(request,'update.html',{'values':data,'value':data2})


