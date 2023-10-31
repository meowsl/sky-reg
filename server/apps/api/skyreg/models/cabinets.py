from django.db import models
from django.utils.translation import gettext_lazy as _


class Cabinets(models.Model):
  NUM_FLOOR = [
    (0, 'Цокольный'),
    (1, 'Первый'),
    (2, 'Второй')
    ]
  cabinet_num = models.IntegerField(
    blank=False,
    null=True,
    verbose_name=_("Номер кабинета")
  )
  cabinet_floor = models.IntegerField(
    choices=NUM_FLOOR,
    blank=False,
    null=True,
    verbose_name=_("Этаж кабинета")
  )

  def __str__(self):
        return f'Этаж - {self.cabinet_floor}, Кабинет - {self.cabinet_num}'

  class Meta:
      verbose_name = _("Кабинет")
      verbose_name_plural = _("Кабинеты")