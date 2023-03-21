from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="Название",
        null=False,
        blank=False
    )
    description = models.TextField(
        max_length=500,
        verbose_name="Описание",
        null=False,
        blank=False
    )
    user = models.ManyToManyField(
        through='webapp.User',
        related_name='project',
        verbose_name='Пользователь',
        to=User
    )
    start_date = models.DateField(
        verbose_name="Начало",
        null=False,
        blank=False
    )
    end_date = models.DateField(
        verbose_name="Конец",
        null=True,
        blank=True
    )
    is_deleted = models.BooleanField(
        verbose_name='Удалено',
        null=False,
        default=False,
    )

    def __str__(self):
        return self.title
