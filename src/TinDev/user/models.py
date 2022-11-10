from django.db import models

# Create your models here.


class User(models.Model):
    '''Every user is represented in the class'''
    USER_TYPES = [('Recruiter', 'recruiter'), ('Candidate', 'candidate')]
    name = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    user_type = models.CharField(
        max_length=9, choices=USER_TYPES)

    # Candidate Types
    profile_bio = models.TextField(max_length=500, blank=True)
    education = models.TextField(blank=True)
    github = models.CharField(max_length=50, blank=True)
    experience = models.IntegerField(null=True)
    skills = models.TextField(null=True)

    # Recruiter
    company = models.CharField(max_length=50, null=True)
