from django.shortcuts import render, redirect
from .models import Project, Project_image, Rating
from users.models import Profile

def show_projects(request):
    projects = Project.get_all_projects()
    project_images = Project_image.objects.all()

    context = {}
    context['projects'] = projects
    context['project_images'] = project_images
    return render(request, 'project_app/Projects.html',context)

def add_rating(request):

    if request.method == 'GET':
        rating = request.GET.get('rating')
        project_ = request.GET.get('project')

        project = Project.objects.get(id=project_)
        print(project_)
        rate = Rating(project_title=project, user=request.user, rate=rating)
        rate.save()

        return redirect('show_projects')