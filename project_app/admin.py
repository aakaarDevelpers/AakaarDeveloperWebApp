from django.contrib import admin
from .models import Project, Project_image, Rating

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_title', 'price', 'like']

@admin.register(Project_image)
class Project_imageAdmin(admin.ModelAdmin):
    list_display = ['project_title']

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'project_title', 'user', 'rate']