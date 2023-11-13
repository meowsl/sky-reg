from django.db import models
from django.utils.translation import gettext_lazy as _
from .rnd_cabinets import RNDCabinets

class RNDSchedule(models.Model):

  class AppointmentType(models.IntegerChoices):
    PRIMARY = 1, _("Первичный")
    SECONDARY = 2, _("Вторичный")
    LEARN = 3, _("Обучение")

  client = models.CharField(
    max_length=150,
    blank=False,
    null=True,
    verbose_name=_("Данные клиента")
  )

  date = models.DateField(
    blank = False,
    default = None,
    verbose_name = _('Дата записи ')
  )

  typePriem = models.PositiveIntegerField(
    choices=AppointmentType.choices,
    blank=False,
    null=True,
    verbose_name=_("Тип приема")
  )

  cabinet = models.ForeignKey(
    RNDCabinets,
    null=True,
    verbose_name=_("Кабинет"),
    on_delete=models.CASCADE,
  )

  def __str__(self):
    return f'Дата: {date} / Тип приема: {typePriem}'

  class Meta:
    verbose_name=_("Расписание, Краснодар")
    verbose_name_plural=_("Расписание, Краснодар")