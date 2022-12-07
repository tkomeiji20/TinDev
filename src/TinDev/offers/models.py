from django.db import models
from posts.models import Post
from user.models import User
import datetime


# Create your models here.
class Offers(models.Model):
    salary = models.IntegerField()
    expiration = models.DateTimeField(default=datetime.datetime(2023, 12, 31, 11, 59, 59))

    # TODO: Further Thinking this should be Many to One fields
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
