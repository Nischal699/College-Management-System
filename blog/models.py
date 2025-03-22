from django.db import models

class Blog(models.Model):
    blog_image=models.ImageField(upload_to='blog_images/',default=None)
    blog_title=models.CharField(max_length=50)
    blog_des=models.TextField()

