from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator, BaseValidator


class StatusChoice(models.TextChoices):
    ACTIVE = 'ACTIVE', 'Активно'
    NOT_ACTIVE = 'NOT_ACTIVE', 'Не активно'


class CustomDescriptionValidator(BaseValidator):
    def __init__(self, limit_value=30):
        message = 'Максимальная длина заголовка %(limit_value)s. Вы ввели %(show_value)s символов'
        super().__init__(limit_value=limit_value, message=message)

    def compare(self, value, limit_value):
        return value > limit_value

    def clean(self, value):
        return len(value)


class CustomDetailedValidator(BaseValidator):
    def __init__(self, limit_value=100):
        message = 'Максимальная длина %(limit_value)s. Вы ввели %(show_value)s символов'
        super().__init__(limit_value=limit_value, message=message)

    def compare(self, value, limit_value):
        return value > limit_value

    def clean(self, value):
        return len(value)


class Task(models.Model):
    description = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="Описание",
        validators=(MinLengthValidator(limit_value=2, message='Слишком короткое описание!'), CustomDescriptionValidator())
    )
    detailed_description = models.TextField(
        max_length=2000,
        null=True,
        blank=True,
        verbose_name="Детально",
        validators=(MinLengthValidator(limit_value=5, message='Необходимо ввести больше 5 символов!'), CustomDetailedValidator())
    )
    status = models.ForeignKey(
        to="webapp.Status",
        on_delete=models.PROTECT,
    )
    type = models.ManyToManyField(
        to="webapp.Type"
    )
    project = models.ForeignKey(
        to="webapp.Project",
        on_delete=models.CASCADE,
        related_name="task",
        verbose_name="Проект"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время и дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Время и дата обновления"
    )
    is_deleted = models.BooleanField(
        verbose_name='Удалено',
        null=False,
        default=False
    )
    deleted_at = models.DateTimeField(
        verbose_name="Время и дата удаления",
        null=True,
        default=None
    )

    def __str__(self):
        return f"{self.description} - {self.status}"

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задание'