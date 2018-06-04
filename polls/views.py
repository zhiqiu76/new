from django.shortcuts import render,redirect
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader


def index(request):
    # 加载模板，指定模板，返回模板对象
    template = loader.get_template('polls_index.html')
    # 构造上下文对象
    context = {'msg': 'Hello World'}
    # 渲染模板并响应
    return HttpResponse(template.render(context))

# 输出文本
def detail(request):
    reponse = HttpResponse("这是一个Detail页面", status=404, content_type="text/plain")
    return reponse

# 输出json
import json
def json_request(request):
    p = {'id': 123, 'userName':'这是一个json数据'}
    reponse = HttpResponse(json.dumps(p), status=200, content_type="application/json", charset="utf-8")
    return reponse


# 输出图片
def image_request(request):
    with open("C:\\Users\\Administrator\\Desktop\\a.jpg", 'rb') as f:
        response = HttpResponse(f.read(), content_type="image/jpeg")
        return response


def redirectTest1(request):
    # return HttpResponseRedirect('/polls/redirectTest2')
    return redirect('/polls/redirectTest2')


def redirectTest2(request):
    return HttpResponse("重定向的页面")

def execute_json(request):
    return JsonResponse({"userName": "张同学", "gender": 1})

# 设置
def set_cookie(request):
    t = request.GET.get('type')
    print(type(t))
    t = int(t)
    template = loader.get_template("test_cookie.html")
    response = HttpResponse(template.render())
    if t == 1: # 设置key-valuecookie
        from urllib import parse
        s = parse.quote("Hello!@#$$%^& World, 上海sxt", encoding="utf-8")
        response.set_cookie("test_cookie", s)
    elif t == 2: # 设置过期时间
        response.set_cookie("cookie_max_age", 123, max_age=10)
    elif t== 3: #设置expires,会让max_age无效
        import datetime
        response.set_cookie("cookie_expires", 234, max_age=10000, expires=datetime.datetime(2020, 12, 1))
    elif t == 4: # 设置path,只能在设置的路劲下访问，不同路径下key相同也是两个cookie, path默认/是根路径都可以访问
        response.set_cookie("cookie_path1", 1234, path="/polls/redirectTest2/")
    elif t == 5: # 设置域名，只能在当前域名下访问，如果是顶级域名，那么子域名下都能访问
        response.set_cookie("cookie_domain", 3455, domain="www.shsxt.com")
    elif t == 6: # 设置安全secure，只能在https中进行测试
        response.set_cookie("cookie_secure", 333, secure=True)
    elif t == 7: # 设置httponly，不能用js操作cookie
        response.set_cookie("cookie_httponly", 3443, httponly=True)
    else: # 使用set_signed_cookie()是给cookie的value加密，要穿如salt
        response.set_signed_cookie("cookie_sign", 3234234, salt="shsxt")
    return response



#读所有的cookie
def read_cookie(request):
    cookies = request.COOKIES
    key = request.GET.get('key')
    ty = request.GET.get('type')
    if not ty:
        for k, v in cookies.items():
            print("cookie的key值：%s, value值：%s" % (k, v))
        return render(request, "cookie_read.html", {'cookies': cookies})
    else:
        return HttpResponse("获取到的cookie值：%s" % cookies.get(key))


# 读取某个cookie
def read_some_cookie(request):
    key = request.GET.get('key')
    salt = request.GET.get('salt', '')
    value = request.get_signed_cookie(key, salt=salt)
    return HttpResponse("获取到的cookie值：%s" % value)


def delete_cookie(request):
    key = request.GET.get('key')
    response = HttpResponse("删除%s的cookie" % key)
    response.delete_cookie(key)
    return response

def js_cookie(request):
    return render(request, "js_cookie.html")
