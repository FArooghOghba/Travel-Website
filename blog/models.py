from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='blog_post/', default='blog_post/default.jpg')
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ManyToManyField(to=Category)
    tags = TaggableManager()
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    publish_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish_date']

    def snippet(self):
        words = self.content.split()[:30]
        return f'{" ".join(words)} ...'

    def get_absolute_url(self):
        return reverse('blog:single', kwargs={'post_id': self.id})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-approved', '-created_date']

    def __str__(self):
        return self.subject
