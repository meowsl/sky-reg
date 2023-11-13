from django.db import models
from django.utils.translation import gettext_lazy as _


class RNDCabinets(models.Model):

  cabinet_num = models.IntegerField(
    blank=False,
    null=True,
    verbose_name=_("Номер кабинета")
  )
  def __str__(self):
        return f'Кабинет - {self.cabinet_num}'

  class Meta:
      verbose_name = _("Кабинет, Ростов-на-Дону")
      verbose_name_plural = _("Кабинеты, Ростов-на-Дону")