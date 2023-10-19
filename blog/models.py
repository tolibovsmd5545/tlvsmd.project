from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    body = models.TextField()
    data = models.DateTimeField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)])

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    name = models.CharField('Ism', max_length= 50)
    email = models.EmailField()
    text = models.TextField('matn',max_length=200)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('article_list')