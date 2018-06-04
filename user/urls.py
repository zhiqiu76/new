from django.urls import path
from . import views
from django.views.generic.base import RedirectView
app_name = 'user'
urlpatterns = [
    path('test1/', views.getTest1, name="test1"),
    path('test2/', views.getTest2, name="test2"),
    path('test3/', views.getTest3, name="test3"),

    path('register/', views.register, name="register"),
    path('do_register/', views.do_register, name="do_register"),


    path('welcome/', views.welcome, name="welcome"),
    path('login/', views.login, name="login"),
    path('do_login/', views.do_login, name="do_login"),
    path('logout/', views.logout, name="logout"),

    path("", views.UserView.as_view(), name=""),
    path("home/", views.HomeView.as_view(), name="home"),

    path('go-to-django/', RedirectView.as_view(url='https://djangoproject.com'), name='go-to-django'),
    path("redirect/", views.RedirectTestView.as_view(), name="redirect"),

    path("list/", views.UserListView.as_view(), name="list"),
    path("detail/<int:pk>/", views.UserDetailView.as_view(), name="detail"),
    # path("detail/<slug:slugUrl>/", views.UserDetailView.as_view(), name="detail")

    path('template/', views.return_template, name="template")

]
