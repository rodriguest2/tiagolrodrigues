from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=2000)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=200)
    post_img = models.ImageField(upload_to='')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        #redirecting to detailed view of newly created post
        return reverse('post_detail', args=(str(self.id)))



class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index')



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.post.title, self.name)
