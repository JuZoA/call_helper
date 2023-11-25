from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class BaseDictModelMixin(models.Model):
    code = models.CharField('код', max_length=16, primary_key=True)
    name = models.CharField('Название', max_length=32,)
    sort = models.PositiveSmallIntegerField('Сортировка', null=True, blank=True)
    is_active = models.BooleanField('Активность', default=True)


    class Meta:
        ordering = ('sort',)
        abstract = True
    

    def __str__(self) -> str:
        return f'{self.code} - {self.name}'