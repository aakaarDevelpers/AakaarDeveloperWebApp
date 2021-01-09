from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# from blog.models import BlogPost

def my_admin_homepage(request):
    # users = User.objects.all()[:5]
    # blogs = BlogPost.objects.all()[:5]

    context ={}
    # context['users'] = users
    # context['blogs'] = blogs
    return render(request, 'my_admin/dashboard.html', context)

def delete_blog(request, *args, **kwargs):
    # blog_id = int(kwargs.get('id'))
    # blog = BlogPost.objects.get(id=blog_id)
    # blog.delete()

    return redirect('admin_home')