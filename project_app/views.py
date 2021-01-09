from django.shortcuts import render
from .models import Project, Project_image

def show_projects(request):
    projects = Project.get_all_projects()
    project_images = Project_image.objects.all()

    context = {}
    context['projects'] = projects
    context['project_images'] = project_images
    return render(request, 'project_app/Projects.html',context)