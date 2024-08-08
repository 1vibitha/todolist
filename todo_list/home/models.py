from django.db import models
# Create your models here.
class tasks(models.Model):
    tasktitle = models.CharField(max_length=30)
    taskdesc = models.TextField()
    time=models.DateTimeField(auto_now_add=True)
    
