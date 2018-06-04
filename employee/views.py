from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from employee.models import Dept, Emp, SalGrade
from django.db import transaction
# Create your views here.


# @transaction.atomic
# def add(request):
#     d1 = Dept(dname='服务器', loc='上海')
#     d1.save()
#     raise Exception
#     d2 = Dept(dname='服务器2', loc='上海2')
#     d2.save()

# def add(request):
#     with transaction.atomic():
#         d1 = Dept(dname='服务器', loc='上海')
#         d1.save()
#         raise Exception
#         d2 = Dept(dname='服务器2', loc='上海2')
#         d2.save()


@transaction.non_atomic_requests
def add(request):

    d1 = Dept(dname='服务器', loc='上海')
    d1.save()
    raise Exception
    d2 = Dept(dname='服务器2', loc='上海2')
    d2.save()


from django.shortcuts import reverse
# 查询所有的雇员信息
def list_emps(request):
    # 查询数据
    emps = Emp.objects.all()
    return render(request, "emp_list.html", context={'items':emps})

# 展示所有的部门信息
def list_dept(request):
    depts = Dept.objects.all()
    return render(request, "dept_list.html", {"items": depts})

# 通用视图
def list(request, model):
    objs = model.objects.all()
    return render(request, "%s_list.html" % model.__name__.lower(), {"items": objs})


def rs(request, id):
    return HttpResponse("这是重定向过来的地址：%d" % id)


def test1(request):
    # 重新发送到rs视图控制器
    return HttpResponseRedirect(reverse("employee:test_rs", args=(123, )))


import json
from django.views.decorators.csrf import csrf_exempt


def findSalGrade(request):
    # 先获取参数
    # id = request.GET.get('id')
    id = request.POST.get('id')
    # id = request.REQUEST.get('id') # 既可以获取post也可以获取get
    # 查询数据库
    try:
        s = SalGrade.objects.get(pk=id)
        result = {"code": 200, "message": "Success!", "results": s.grade}
    except Exception:
        result = {"code": 500, "message": "该等级不存在!", "results": '该等级不存在!'}
    # return HttpResponse(json.dumps(result), content_type="application/json;charset=utf-8") # 返回一个json字符串
    return JsonResponse(result)
