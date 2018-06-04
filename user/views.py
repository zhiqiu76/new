from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST
from django.utils import timezone
from .models import UserInfo
# Create your views here.

def getTest1(request):
    return render(request,'user/getTest1.html')


@require_GET
def getTest2(request):
    # 接收参数
    a = request.GET['a']
    b = request.GET['b']
    return render(request,'user/getTest2.html', {"a": a, "b": b})


@require_GET
def getTest3(request):
    a = request.GET.getlist("a")
    b = request.GET.get('b')
    return render(request,'user/getTest3.html', {"a": a, "b": b})

# 注册页面
@require_GET
def register(request):
    return render(request, "user/register.html")


# 提交用户注册的数据
@require_POST
def do_register(request):
    # 先获取参数
    uname = request.POST.get('uname')
    upwd = request.POST.get('upwd')
    gender = request.POST.get('gender')
    interests = request.POST.getlist('interest')

    # 把数据存入数据库
    return render(request, "user/register_success.html", {'uname':uname, 'upwd':upwd,
                                    'gender':gender, 'interests': ', '.join(interests)})


# 首页
def welcome(request):
    se = request.session
    print(se)
    login_user_name = se.get('login_user_name')
    return render(request, "welcome.html", {'login_user_name': login_user_name})

# 登录页面
def login(request):
    # 先判断是否登录，如果登录直接跳转到首页
    if request.session.get('login_user_name'):
        return redirect("/user/welcome")
    return render(request, "login.html")

# 登录的业务逻辑
def do_login(request):
    # 获取登录用户名、密码
    user_name = request.POST.get('userName')
    password = request.POST.get('password')
    # 基本参数校验

    if not user_name or len(user_name.strip()) == 0:
        return render(request, "login.html", {'message': '请输入用户名'})

    if not password:
        return render(request, "login.html", {'message': '请输入密码',  'userName': user_name})
    # 先判断是否登录，如果登录直接跳转到首页
    if request.session.get('login_user_name'):
        return redirect("/user/welcome")
    # 数据库进行匹配
    user = UserInfo.objects.filter(userName=user_name.strip()).filter(password=password)
    if not user:
        return render(request, "login.html", {'message': '用户名和密码错误！',
                                              'userName': user_name, 'password':password})

    # 成功就将用户名写入session
    request.session['login_user_name'] = user_name

    # 设置过期时间
    # 浏览器关闭失效
    request.session.set_expiry(0)

    return redirect("/user/welcome")

# 注销逻辑
def logout(request):
    # 把userName从当前的session移除
    # del request.session['login_user_name']
    request.session.flush()
    return redirect("/user/welcome")



from django.views.generic.base import View
from django.http.response import HttpResponse
from django.contrib import messages
class UserView(View):

    def get(self, request, *args, **kwargs): # 用户获取资源
        print("这是一个get请求")
        # return HttpResponse("这是一个get请求。。。")
        # raise Exception
        messages.warning(request, "这是一个warning message")
        return render(request, "test_message.html")
    def post(self, request, *args, **kwargs): # 用户添加资源
        return HttpResponse("这是一个Post请求。。。")

    def put(self, request, *args, **kwargs): # 用户修改资源
        return HttpResponse("这是一个Put请求。。。")

    def delete(self, request, *args, **kwargs): # 删除资源
        return HttpResponse("这是一个Delete请求。。。")

    # 处理不支持的请求方式
    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse("方法不支持。。。")


from django.views.generic.base import TemplateView
class HomeView(TemplateView):
    template_name = "home.html"

    # 定制返回给页面的数据
    def get_context_data(self, **kwargs):
        # 查询数据
        return {"userName": 'Tonygogo'}

    def post(self, request, *args, **kwargs):
        return HttpResponse("设置POST请求")


from django.views.generic.base import RedirectView
class RedirectTestView(RedirectView):
    # pattern_name = "user:home" # 反向解析的地址
    url = 'http://127.0.0.1:8000/user/home'
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        # 业务逻辑
        return super().get_redirect_url(*args, **kwargs)

from django.views.generic.list import ListView
from django.db.models import QuerySet
class UserListView(ListView):
    # model = UserInfo # 查询的模型
    queryset = QuerySet(UserInfo)
    template_name = "user_list.html"
    context_object_name = 'users'

    # 重写 修改获取数据的方法
    # def get_queryset(self):
    #     return UserInfo.objects.filter(userName='张三')

    # 重写，修改输出的内容
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     return {"users": self.get_queryset()}


from django.views.generic.detail import DetailView
class UserDetailView(DetailView):
    model = UserInfo # 模型名字
    template_name = "user_detail.html" # 模板名称, 默认是app_lable/modelname_detail.html
    pk_url_kwarg = 'id' # 根据主键查询的字段名，默认是pk
    context_object_name = "user" # 使用object或者模块小写
    slug_field = 'slugUrl' # 匹配模型中的slug属性
    slug_url_kwarg = "slugUrl" # 匹配url中参数


from django.template.response import TemplateResponse
def return_template(request):
    raise Exception
    return TemplateResponse(request, "home.html", {'userName':'Tonygogo'})