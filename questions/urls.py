from django.urls import path
from . import views

app_name = 'questions'


urlpatterns = [
    path('index', views.index, name="index"),
    path('detail', views.detail, name="detail"),
    path('list', views.list, name="list"),
]