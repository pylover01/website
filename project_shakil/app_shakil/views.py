from django.http.response import HttpResponse, Http404
from .models import Blog, Work
from django.shortcuts import render
from django.core.mail import send_mail

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

def send_message(request):
    if request.method == "POST":
        message_name = request.POST['message_name']
        message_email = request.POST['message_email']
        message_phone = request.POST['message_phone']
        message_body = request.POST['message_body']

        send_mail(
            message_name,
            message_email,
            message_phone,
            message_body,
            ['info@service-shakil.com']
        )

        return render(request, 'app_shakil/contact.html', {'message_name':message_name})
    else:
        return render(request, 'app_shakil/contact.html', {})