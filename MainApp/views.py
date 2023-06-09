from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "home.html")

def detection(request):
    return render(request, "test.html")


def result(request):
    name = request.POST.get("name", "Undefined")
    age = request.POST.get("age", 1)
    result={"result":"В вас нема посттравматичного стресового розладу", "panic":request.POST.get("panic")}
    return render(request, "result.html", context=result)
