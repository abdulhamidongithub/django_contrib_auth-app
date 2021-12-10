from django.contrib.auth.models import User
from django.db import models

#Let's say we have clients to be logged in or out
class Client(models.Model):
    G = (
        ("male", "male"),
        ("female", "female")
    )
    name = models.CharField(max_length=25)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=10, choices=G)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name} ({self.age})"

#We are using django.contrib.confirm.model's User class to store client's login and password data