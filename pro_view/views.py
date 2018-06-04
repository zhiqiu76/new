from django.http import HttpResponse
from django.views.generic.base import View


def index(request):
    return HttpResponse("这是咱们的首页")

