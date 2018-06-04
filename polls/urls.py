from django.urls import path
from . import views


urlpatterns = [
    path("index/", views.index, name='index'),
    path("detail/", views.detail, name='detail'),
    path("json/", views.json_request, name='json'),
    path("image_request/", views.image_request, name='image_request'),

    path("redirectTest1/", views.redirectTest1, name='redirectTest1'),
    path("redirectTest2/", views.redirectTest2, name='redirectTest2'),
    path("execute_json/", views.execute_json, name='execute_json'),

    path("set_cookie/", views.set_cookie, name='set_cookie'),
    path("read_cookie/", views.read_cookie, name='read_cookie'),
    path("read_some_cookie/", views.read_some_cookie, name='read_some_cookie'),
    path("delete_cookie/", views.delete_cookie, name='delete_cookie'),
    path("js_cookie/", views.js_cookie, name='js_cookie'),
]
