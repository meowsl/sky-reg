from django.db import models
from django.utils.translation import gettext_lazy as _


class KRDSchedule(models.Model):

  class AppointmentType(models.IntegerChoices):
    PRIMARY = 1, _("Первичный")
    SECONDARY = 2, _("Вторичный")
    LEARN = 3, _("Обучение")

  TIMES = (
    ('10:00','10:00'),
    ('10:30','10:30'),
    ("11:00","11:00"),
    ("11:30","11:30"),
    ("12:00","12:00"),
    ("12:30","12:30"),
    ("13:00","13:00"),
    ("13:30","13:30"),
    ("14:00","14:00"),
    ("14:30","14:30"),
    ("15:00","15:00"),
    ("15:30","15:30"),
    ("16:00","16:00"),
    ("16:30","16:30"),
    ("17:00","17:00"),
    ("17:30","17:30"),
    ("18:00","18:00"),
    ("18:30","18:30"),
  )


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

  time = models.CharField(
    max_length=5,
    choices=TIMES,
    blank=False,
    null=True,
    unique=True,
    verbose_name=_("Время")
  )

  typePriem = models.PositiveIntegerField(
    choices=AppointmentType.choices,
    blank=False,
    null=True,
    verbose_name=_("Тип приема")
  )

  def __str__(self):
    return f'Дата: {self.date} / Тип приема: {self.typePriem}'

  class Meta:
    verbose_name=_("Расписание, Краснодар")
    verbose_name_plural=_("Расписание, Краснодар")