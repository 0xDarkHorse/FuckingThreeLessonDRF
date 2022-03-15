# FUCK Project-Django FUCK
# Without a clear technical specification, the result of WTF

from django.db import models
from django.utils import timezone
from main.models import Users   # ?


class Projects(models.Model):
    fuck_name = models.CharField(max_length=20)
    url_git = models.URLField()
    authors = models.ManyToManyField(Users, related_name="authors")


class TODO(models.Model):
    project = models.OneToOneField(
        Projects,
        on_delete=models.CASCADE
    )
    text = models.TextField()
    data_create = models.DateTimeField(auto_now_add=True)
    data_edit = models.DateTimeField(auto_now=True)
    author = models.OneToOneField(
        Users,
        on_delete=models.SET_DEFAULT,
        default="[Fuck] - Автор удален!",
        related_name="author"
    )
    enabled = models.BooleanField(default=True)
