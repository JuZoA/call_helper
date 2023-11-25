from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class ReplacementStatus(models.Model):
    code = models.CharField('код', max_length=16, primary_key=True)
    name = models.CharField('Название', max_length=32,)
    sort = models.PositiveSmallIntegerField('Сортировка', null=True, blank=True)
    is_active = models.BooleanField('Активность', default=True)
    class Meta:
        verbose_name = 'стаус смены'
        verbose_name_plural = 'статусы смены'
        ordering = ('sort',)

    def __str__(self) -> str:
        return f'{self.code} - {self.name}'
    


class Replacement(models.Model):
    group = models.ForeignKey(
        'breaks.Group', on_delete=models.CASCADE, related_name='replacements',
        verbose_name='Группа',
    )
    date = models.DateField('Дата смены')
    break_start = models.TimeField('Начало обеда')
    break_end = models.TimeField('Конец обеда')
    break_max_duration = models.PositiveBigIntegerField(
        'Макс. продолжительность обеда',
    )
    class Meta:
        verbose_name = 'Смена'
        verbose_name_plural = 'Смены'
        ordering = ('-date',)

    def __str__(self) -> str:
        return f'Сменя для {self.group}'


class ReplacementEmployee(models.Model):
    employee = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='replacements',
        verbose_name='Сотрудник',
    )
    replacement = models.ForeignKey(
        'breaks.Replacement', on_delete=models.CASCADE, related_name='employees',
        verbose_name='Смена',
    )
    status = models.ForeignKey(
        'breaks.ReplacementStatus', on_delete=models.CASCADE, related_name='remplacement_employees',
        verbose_name='Статус смены',
    )

    class Meta:
        verbose_name = 'Смена - Работник'
        verbose_name_plural = 'Смены - Работники'

    def __str__(self) -> str:
        return f'Сменя {self.replacement} для {self.employee}'
