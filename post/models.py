from django.db import models

# Create your models here.

<<<<<<< HEAD
=======
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #image = models.ImageField(upload_to='images/', blank=True)
    
    def __str__(self):
        return self.title
    
>>>>>>> feature/post
