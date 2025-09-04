from django.db import models

# Create your models here.
class KMB_Blog(models.Model):
    blog_img = models.ImageField()
    blog_title = models.CharField(max_length=20)
    blog_description = models.TextField()
    
    def __str__(self) -> str:
        return self.blog_title
    
class Contact_Us(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()
    
    def __str__(self) -> str:
        return self.name