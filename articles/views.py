from django.shortcuts import render
import datetime
from django.http import HttpResponse
# Create your views here.


def special_case_2003(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def year_archive(request, year):
    html = "按年归档：%s" % year
    return HttpResponse(html)


def month_archive(request, year, month):
    html = "按月归档：%s_%s" % (year, month)
    return HttpResponse(html)


def article_detail(request, year=2003, month=3,
                   slug="building-a-django-site"):
    html = "详情页：%s_%s_%s" % (year, month, slug)
    return HttpResponse(html)

from django.views.decorators.http import require_http_methods, require_POST, require_GET, require_safe

# 添加
@require_POST
def add(request):
    return HttpResponse("添加数据。。")


# 删除
@require_http_methods(["DELETE"])
def delete(request):
    return HttpResponse("删除数据。。")


# 修改
from django.http.request import QueryDict
@require_http_methods(["POST", "PUT", "DELETE"])
def update(request):
    params = request.body
    q = QueryDict(params.decode("utf-8")) # str(params, encoding='utf-8')
    print(q.get("id"))
    print(q.get("name"))
    return HttpResponse("修改数据。。")


# 查询
@require_GET
def find(request):
    return HttpResponse("获取数据。。")

# 查询
@require_safe
def safe(request):
    return HttpResponse("安全获取数据。。")
