from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def test01(request, id):
    return HttpResponse("这是一个Test!!!---%d" % (id))


def request_test(request):

    return render(request, "request_test.html", {'request': request})