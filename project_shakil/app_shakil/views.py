from .models import Blog
from django.shortcuts import render

def index(request):
    return render(request, 'app_shakil/index.html')

def contact(request):
    return render(request, 'app_shakil/contact.html')

def work(request):
    return render(request, 'app_shakil/work.html')

def blog(request):
    latest_blog_data = Blog.objects.order_by('-blog_dateTime')
    context = {'latest_blog_data': latest_blog_data,}
    return render(request, 'app_shakil/blog.html', context)