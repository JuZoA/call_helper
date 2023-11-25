from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Break(models.Model):
    replacement = models.ForeignKey(
        'breaks.Replacement', on_delete=models.CASCADE,
        related_name='breaks', verbose_name='смена',
    )
    employee = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='breaks',
        verbose_name='Сотрудник',
    )
    break_start = models.TimeField('Начало обеда', null=True, blank=True, )
    break_end = models.TimeField('Конец обеда', null=True, blank=True, )
    status = models.ForeignKey(
        'breaks.BreakStatus', models.RESTRICT,
        related_name='breaks', verbose_name='Статус',
        blank=True,
    )

    class Meta:
        verbose_name = 'Обеденный перервы'
        verbose_name_plural = 'Обеденные перерывы'
        ordering = ('-replacement__date', 'break_start')

    def __str__(self) -> str:
        return f'Обед пользователя - {self.employee}'