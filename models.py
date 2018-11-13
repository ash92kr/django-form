from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=100)
    
    def __stf__(self):
        return self.title