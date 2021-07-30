from django.shortcuts import render

def index(request):
    return render(request, 'app_shakil/index.html')

def contact(request):
    return render(request, 'app_shakil/contact.html')

def work(request):
    return render(request, 'app_shakil/work.html')

def blog(request):
    return render(request, 'app_shakil/blog.html')