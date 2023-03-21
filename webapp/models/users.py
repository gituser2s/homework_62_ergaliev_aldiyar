from django.contrib.auth.models import User
from django.db import models
from webapp.models import Project


class User(models.Model):
    user = models.ForeignKey(
        to=User,
        related_name='projects',
        verbose_name='Избранное',
        null=False,
        on_delete=models.CASCADE
    )
    project = models.ForeignKey(
        to=Project,
        related_name='users',
        verbose_name='Избранное',
        null=False,
        on_delete=models.CASCADE
    )
