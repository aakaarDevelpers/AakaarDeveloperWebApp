from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    category = models.CharField(max_length=30, null=True, blank=True)
    body = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to='Blogs/thumbnails/', null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @staticmethod
    def get_all_blogs():
        return BlogPost.objects.all()

    @staticmethod
    def get_all_blog_count():
        return BlogPost.objects.all().count()