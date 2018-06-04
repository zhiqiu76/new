from django.shortcuts import render
from .models import Question

# Create your views here.
def index(request):
    questions = Question.objects.all()
    return render(request, "index.html", {"questions":questions,
                                          'users':[], 'username':'<h1>Hello</h1>'})


def detail(request):
    return render(request, 'detail.html')


def list(request):
    return render(request, "list.html")