from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Organisation(models.Model):
    name = models.CharField('Название', max_length=255)
    director = models.ForeignKey(
        User, on_delete=models.RESTRICT, related_name='organisation_directors',
        verbose_name='Директор',
    )
    employees = models.ManyToManyField(
        User, related_name='organisation_employees', verbose_name='Сотрудники',
        blank=True,
    )

    class Meta:
        verbose_name = 'Ораганизация'
        verbose_name_plural = 'Организации'
        ordering = ('name',)

    def __str__(self) -> str:
        return self.name

