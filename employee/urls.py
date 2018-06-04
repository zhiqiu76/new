from django.urls import path

from .models import *
from . import views

app_name = 'employee'

urlpatterns = [
    # path('list_emps/', views.list_emps, name="list"),
    # path('list_depts/', views.list_dept, name="list_depts"),
    path('list_emps/', views.list, {"model": Emp}, name="list"),
    path('list_depts/', views.list,{"model": Dept},name="list_depts"),
    path('rs/<int:id>', views.rs, name="test_rs"),
    path('test/', views.test1, name="test1"),

    path('findSalGrade/', views.findSalGrade, name="findSalGrade"),
]