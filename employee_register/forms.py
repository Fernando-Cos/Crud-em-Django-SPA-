from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
         model = Employee
         fields = ('fullname','mobile', 'emp_code', 'position')
         labels = {
             'fullname': 'Nome Completo',
             'emp_code':'Codigo',
             'mobile': 'Telefone',
             'position': 'Cargo'
         }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Selecione"
        self.fields['emp_code'].required = False