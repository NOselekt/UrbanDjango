from django.shortcuts import render

# Create your views here.

def class_view(request):
    return render(request, "class_template.html")

def func_view(request):
    return render(request, "func_template.html")