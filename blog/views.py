from django.shortcuts import render
from .models import BlogPost

def blog_posts(request):
    blogs = BlogPost.get_all_blogs()
    context = {'blogs': blogs}
    return render(request, 'blog/blog.html', context)