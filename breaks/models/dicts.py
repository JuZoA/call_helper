from django.db import models
from django.contrib.auth import get_user_model
from common.models.mixins import BaseDictModelMixin


User = get_user_model()


class ReplacementStatus(BaseDictModelMixin):
    class Meta:
        verbose_name = 'стаус смены'
        verbose_name_plural = 'статусы смены'


class BreakStatus(BaseDictModelMixin):
    class Meta:
        verbose_name = 'стаус обеда'
        verbose_name_plural = 'статусы обеда'
