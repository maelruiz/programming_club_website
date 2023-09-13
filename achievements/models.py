from django.db import models
from django.contrib.auth.models import User

class Achievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_achieved = models.DateTimeField(auto_now_add=True)
    points = models.CharField(max_length=50)

    def __str__(self):
        return self.title
