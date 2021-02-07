from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Function(models.Model):
    command = models.TextField()

    date = models.DateField(
        null=True,
        default=datetime.now()
    )

    user = models.ForeignKey(
        User,
        default=User,
        on_delete=models.CASCADE,
        null=True)

    folder = models.TextField(default="Folder")
    title = models.TextField(default="Function 1")