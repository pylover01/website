from django.shortcuts import render

def index(request):
    return render(request, 'app_shakil/index.html')

def contact(request):
    return render(request, 'app_shakil/contact.html')