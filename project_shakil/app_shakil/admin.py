from django.contrib import admin
from .models import Users, Blog, Work

# Register your models here.



class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Image', {'fields' : ['blog_image']}),
        ('Title', {'fields' : ['blog_title']}),
        ('Body', {'fields' : ['blog_body']}),
        ('Date', {'fields' : ['blog_dateTime']}),
        ('Blog Type', {'fields' : ['blog_type']}),
    ]

    list_filter = ['blog_dateTime']

    search_fields = ['blog_title']

    list_display = ('blog_title', 'blog_dateTime', 'blog_type')

class WorkAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Image', {'fields' : ['work_image']}),
        ('Title', {'fields' : ['work_title']}),
        ('Body', {'fields' : ['work_tools']}),
        ('Date', {'fields' : ['work_url']}),
    ]
    list_display = ('work_title', 'work_tools', 'work_url')


admin.site.register(Users)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Work, WorkAdmin)

