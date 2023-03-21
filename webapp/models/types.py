from django.db import models


class Type(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="Тип",
        null=False,
        blank=False
    )

    def __str__(self):
        return self.title
