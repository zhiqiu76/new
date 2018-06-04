from django.urls import path,re_path
from . import views


urlpatterns = [
    path('blog/', views.page),
    path('blog/page<int:num>/', views.page),
    re_path(r'^blog/page-(?P<page_number>\d+)/$', views.blog_articles),

    path('blog/add', views.add),
    path('blog/update', views.update),
    path('blog/delete', views.delete),

]
