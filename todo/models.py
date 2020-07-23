from django.db import models

# Create your models here.

PRIORITY = (('danger','hight'),('info','nomal'),('success','low'))
class TodoModel(models.Model): # couese-31
    title = models.CharField(max_length=100) # couese-31
    memo = models.TextField() # couese-31
    priority = models.CharField(
        max_length = 50,
        choices = PRIORITY
    )
    duedate = models.DateField()
    def __str__(self): # couese-34
        return self.title # couese-34