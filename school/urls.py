from django.urls import path
from . import views

app_name = 'school'

urlpatterns = [
    path("jsonp/", views.jsonp, name='jsonp'),
    path("do_jsonp/", views.do_jsonp, name='do_jsonp'),
    path("load_github/", views.load_github, name='load_github'),
    path("test_csrf/", views.test_csrf, name='test_csrf'),
    path("index/", views.index, name='index'),
    path("register/", views.register, name='register'),

    path("upload_page/", views.upload_page, name='upload_page'),
    path("upload_file/", views.upload_file, name='upload_file'),
]
