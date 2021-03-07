#importando modules
from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
# Create your views here.



#função para a listagem dos users
def employee_list(request):
    context = {'employee_list' :Employee.objects.all()} #selecionando todos os objec do db
    return render(request, "employee_register/employee_list.html", context) #retorno  da lista dentro da variavel context



# função do formulario vai ter 2 metodos que sao o get e o post, para operações de inserção e atualização
def employee_form(request, id = 0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance = employee)
        return render(request, "employee_register/employee_form.html", {'form':form})
    else: 
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance = employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')



# e aqui temos a função de visualização final para excluir um registro de funcionário 
# dentro da função de visualização do formulário de funcionário
def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')

