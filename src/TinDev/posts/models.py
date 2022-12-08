from django.db import models
import datetime
from user.models import User

# Create your models here.
class Post(models.Model):
    JOB_TYPE = [('part', 'Part-Time'), ('full', 'Full-Time')]
    position = models.CharField(max_length=20)
    type = models.CharField(max_length=10, choices=JOB_TYPE)
    location = models.CharField(max_length=50)
    skills = models.TextField()
    description = models.TextField()
    company = models.CharField(max_length=20)
    expiration = models.DateTimeField(default=datetime.datetime(2023, 12, 31, 11, 59, 59))
    status = models.BooleanField(default=True)
    interest = models.ManyToManyField(User)
    recruiter_id = models.IntegerField(default=-1)