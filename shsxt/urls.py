from django.urls import path
from . import views


urlpatterns = [
    path("<int:id>/", views.test01, name='test01'),
    path("request_test/", views.request_test, name='requestion_test')
]
