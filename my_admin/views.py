from django.shortcuts import render
from django.contrib.auth.models import User

def my_admin_homepage(request):
    users = User.objects.all()[:5]
    context ={}
    context['users'] = users
    return render(request, 'my_admin/index.html', context)