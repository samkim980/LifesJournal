from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField


class Article(models.Model):
    title = models.CharField(max_length=200, unique=True)
    article_image = models.ImageField(upload_to='images', blank = True, null =True)
    description = models.CharField(max_length=300)
    author = models.ForeignKey(get_user_model(), on_delete= models.CASCADE, related_name='uploader')
    content = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
    #     # return 'Comment: {} by {}'.format(self.body, self.name)
        return self.body

class Subscribers (models.Model):
    email = models.EmailField(max_length = 254, primary_key=True)
    

    def __str__ (self):
        return self.email
