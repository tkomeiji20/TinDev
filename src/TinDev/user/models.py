from tkinter import Widget
from django.db import models
from django import forms

# Create your models here.


class User(models.Model):
    '''Every user is represented in the class'''
    USER_TYPES = [('recruiter', 'Recruiter'), ('candidate', 'Candidate')]
    name = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    user_type = models.CharField(
        max_length=9, choices=USER_TYPES, default=USER_TYPES[0][1])

    # Candidate Types
    profile_bio = models.TextField(max_length=500, blank=True)
    education = models.TextField(blank=True)
    github = models.CharField(max_length=50, blank=True)
    experience = models.IntegerField(default=1)
    skills = models.TextField(null=True)

    # Recruiter
    company = models.CharField(max_length=50, null=True)
