from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='post_autor')
    blog_title = models.CharField(max_length=264, verbose_name="Put a Title")
    slug = models.SlugField(max_length=264, unique=True)
    blog_content = models.TextField(verbose_name="What is in on mind?")
    blog_image = models.ImageField(upload_to='blog_images', 
                                   verbose_name="Blog Image")
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.blog_title