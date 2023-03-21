from django.db import models


class Status(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="Статус",
        null=False,
        blank=False
    )

    def __str__(self):
        return self.title
