from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee_details
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def work_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('retrieveproduct')
    else:
        form =EmployeeForm()
    return render(request, 'create.html', {'form': form})


@login_required(login_url='/login/')
def work_read(request):
    work_list=Employee_details.objects.all()
    return render(request,'retrieve.html',{'work_list':work_list})

@login_required(login_url='/login/')
def work_update(request, id):
    product = Employee_details.objects.get(pk=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('retrieveproduct')
    else:
        form =EmployeeForm(instance=product)           
    return render(request, 'update.html', {'form': form})

@login_required(login_url='/login/')
def work_delete(request, pk):
    product = get_object_or_404(Employee_details, pk=pk)
    if request.method == 'POST': 
        product.delete()
        return JsonResponse({'message': 'Employee deleted successfully'}, status=204)
    return JsonResponse({'message': 'Method not allowed'}, status=405)






