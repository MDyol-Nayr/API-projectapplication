from django.db import models
class Post(models.Model):
   title = models.CharField(max_length = 50)
   content = models.TextField()

   def __str__(self):
       return self.title
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
