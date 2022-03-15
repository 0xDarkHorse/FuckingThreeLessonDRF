from django.db import models
from uuid import uuid4


class Users(models.Model):
    # uid = models.UUIDField(primary_key=True, default=uuid4)
    email = models.EmailField(primary_key=True, default='')
    username = models.CharField(max_length=15)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
