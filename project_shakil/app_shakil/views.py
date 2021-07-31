from django.http.response import HttpResponse, Http404
from .models import Blog, Work
from django.shortcuts import render

def index(request):
    latest_blog_data = Blog.objects.order_by('-blog_dateTime')
    latest_work_data = Work.objects.all()
    context = {'latest_blog_data': latest_blog_data, 'latest_work_data': latest_work_data}
    return render(request, 'app_shakil/index.html', context)

def contact(request):
    return render(request, 'app_shakil/contact.html')

def work(request):
    latest_work_data = Work.objects.all()
    context = {'latest_work_data': latest_work_data,}
    return render(request, 'app_shakil/work.html', context)

def blog(request):
    latest_blog_data = Blog.objects.order_by('-blog_dateTime')
    context = {'latest_blog_data': latest_blog_data,}
    return render(request, 'app_shakil/blog.html', context)

def blog_details(request, blog_id):
    try:
        blog_data = Blog.objects.get(pk = blog_id)
    except Blog.DoesNotExist:
        raise Http404("Blog does not exist")
    return render(request, 'app_shakil/blog_details.html', {'blog_data': blog_data})
