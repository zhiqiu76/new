from django.shortcuts import render
from django.http.response import HttpResponse
import json

# Create your views here.
def jsonp(request):
    return render(request, "school/index.html")


def do_jsonp(request):
    callback = request.GET.get('callback')
    data = {"code": 200, 'message': 'Success!', "data": '这是测试JSONP跨域'}
    response = None
    if callback: # 代表是跨域请求
        data = json.dumps(data)
        # callback(data)
        print(callback + "(" + data + ")")
        response = HttpResponse(callback + "(" + data + ")", charset='utf-8')
    else: # 正常请求
        response = HttpResponse(json.dumps(data), content_type="application/json; charset=utf-8", charset='utf-8')
    return response


def load_github(request):
    return render(request, "school/github.html")


def test_csrf(request):
    return render(request, "school/csrf.html")


def index(request):
    return render(request, "school/school_index.html")

def register(request):
    return HttpResponse("注册成功！")


# 上传文件的页面
def upload_page(request):
    return render(request, "school/upload_file.html")


# 处理上传文件
def upload_file(request):
    # 请求方法为POST时,进行处理;
    if request.method == "POST":
        # 获取上传的文件,如果没有文件,则默认为None;
        file = request.FILES.get("myfile")
        if file is None:
            return HttpResponse("请选择上传文件!")
        else:
            # 打开特定的文件进行二进制的写操作;
            with open("c:\\temp\\%s" % file.name, 'wb+') as f:
                # 分块写入文件;
                for chunk in file.chunks(): # 每个chunks是2.5M
                    f.write(chunk)
                # f.write(file.read()) # 不适用大文件上传
            return HttpResponse("上传完成!")
    else:
        return render(request, 'upload.html')

