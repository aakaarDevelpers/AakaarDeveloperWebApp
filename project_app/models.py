from django.db import models
from users.models import Profile

class Project(models.Model):
    project_title = models.CharField(max_length=70, null=True, blank=True)
    thumbnail = models.ImageField(upload_to='projects/thumbnail/', null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    youtube_link = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    like = models.IntegerField(blank=True, null=True)
    slug = models.CharField(max_length=20, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.project_title}'

    @staticmethod
    def get_all_projects():
        return Project.objects.all()
    

class Project_image(models.Model):
    project_title = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='projects/project_images/', null=True, blank=True)

    def __str__(self):
        return f'{self.project_title}'

class Rating(models.Model):
    project_title = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    rate = models.IntegerField(null=True, blank=True)