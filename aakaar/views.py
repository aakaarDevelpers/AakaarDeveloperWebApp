from django.shortcuts import render
from blog.models import BlogPost

def index(request):
    blog_len = BlogPost.get_all_blog_count()
    context = {}
    context['blog_len'] = blog_len
    return render(request, 'aakaar/index.html', context)