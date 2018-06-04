from django.shortcuts import render
from django.http import HttpResponse, Http404
# Create your views here.


def page(request, num=11):
    html = "%s" % num
    return HttpResponse(html)

def blog_articles(request, page_number):
    return HttpResponse("查询第%s页数据。。" % page_number)


# 测试404错误
def add(request):
    raise Http404()
    return "添加成功"

# 500是服务器内部错误
def update(request):
    raise Exception
    return HttpResponse("修改数据。。")


from django.core.exceptions import PermissionDenied
# 403错误，没有权限访问资源
def delete(request):
    raise PermissionDenied
    return HttpResponse("这是删除数据。。。")

