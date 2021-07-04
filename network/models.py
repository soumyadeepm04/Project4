from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.base import Model


class User(AbstractUser):
    pass

class Posts(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField()

class Profile(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="profile")
    followers = models.IntegerField()
    following = models.IntegerField()

class Followers(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="blank1")
    follower = models.ForeignKey("User", on_delete = models.CASCADE, related_name="blank2")

class Following(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name = "blank3")
    following = models.ForeignKey("User", on_delete = models.CASCADE, related_name="blank4")