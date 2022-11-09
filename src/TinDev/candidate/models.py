from django.db import models

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=50)
    profile_bio = models.CharField(max_length=500)
    zipcode = models.IntegerField()
    skills = models.TextField()
    github = models.CharField(max_length=20)
    experience = models.IntegerField()
    education = models.TextField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
