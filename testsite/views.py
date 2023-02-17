from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse("This is about page")

def home(request):
    return render(request, 'home.html', {'greeting': 'Hi!'})

def reverse(request):
    text = request.POST.get("textarea")
    text_reverse = text.reverse()
    return HttpResponse(text_reverse)