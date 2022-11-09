from django.db import models

# Create your models here.
class Post(models.Model):
    JOB_TYPE = [('Part-Time', 'part'), ('Full-Time', 'full')]
    position = models.CharField(max_length=20)
    type = models.CharField(max_length=10, choices=JOB_TYPE)
    location = models.CharField(max_length=50)
    skills = models.TextField()
    description = models.TextField()
    company = models.CharField(max_length=20)
    expiration = models.DateTimeField()
    status = models.BooleanField(default=True)