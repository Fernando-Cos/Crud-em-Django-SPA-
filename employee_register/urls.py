from django.urls import path, include
from . import views


# rotas secundarias do projeto
urlpatterns = [
    path('',views.employee_form, name = 'employee_insert'), #get end post for insert 
    path('delete/<int:id>/', views.employee_delete, name = 'employee_delete'),#get end post req. for delete operation
    path('<int:id>/',views.employee_form, name='employee_update'), #get end post req. for update operation
    path('list/',views.employee_list, name = 'employee_list')#get req. retrieve and display all records.
]