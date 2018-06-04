from django.urls import path, re_path, register_converter

from . import views

from . import converters
register_converter(converters.FourDigitYearConverter, 'yyyy')


app_name = 'articles'

urlpatterns = [
    path('articles/2003/', views.special_case_2003),
    # path('articles/<int:year>/', views.year_archive),
    # path('articles/<int:year>/<int:month>/', views.month_archive),
    # path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
    path('articles/<yyyy:year>/', views.year_archive),
    # re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-]+)/$', views.article_detail),

    path('articles/add', views.add, name='add'),
    path('articles/delete', views.delete, name='delete'),
    path('articles/update', views.update, name='update'),
    path('articles/find', views.find, name='find'),
    path('articles/safe', views.safe, name='safe'),
]