from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    date_visited = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.NOT_PROVIDED)

    def __str__(self):
        return self.title
