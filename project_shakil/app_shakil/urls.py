from django.core.mail import send_mail
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('contact/', views.send_message, name='send_message'),
    path('work/', views.work, name='work'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:blog_id>/', views.blog_details, name='blog_details'),
]