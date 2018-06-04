"""pro_view URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.views import debug

urlpatterns = [
    path('questions/', include("questions.urls")),
    path('school/', include("school.urls")),
    path('polls/', include("polls.urls")),
    path('user/', include("user.urls")),
    path('', include("blog.urls")),
    path('', include("articles.urls")),
    path('shsxt/', include("shsxt.urls")),
    path('employee/', include("employee.urls")),
    # path('', debug.default_urlconf),
    path('', views.index),
    path('admin/', admin.site.urls)
]

# handler404 = views.page_not_found
# handler500 = views.server_error
# handler403 = views.no_permission