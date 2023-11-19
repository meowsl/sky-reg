from django.db import models
from django.utils.translation import gettext_lazy as _

class Applications(models.Model):
    TYPE_PRIEM =[
      ('Первичный', 'Первичный'),
      ('Вторичный', 'Вторичный'),
      ('Обучение', 'Обучение')
    ]

    CITIES = [
      ('Ростов-на-Дону', 'Ростов-на-Дону'),
      ('Краснодар', 'Краснодар'),
      ('Сочи', 'Сочи')
    ]

    firstname = models.CharField(
      max_length=30,
      blank=False,
      verbose_name=_("Имя")
    )

    lastname = models.CharField(
      max_length=30,
      blank=False,
      verbose_name=_("Фамилия")
    )

    midname = models.CharField(
      max_length=55,
      null = True,
      blank = True,
      verbose_name=_('Отчество')
    )

    phone = models.CharField(
      max_length=16,
      null=True,
      blank=False,
      verbose_name=_("Номер телефона")
    )

    date = models.DateField(
      blank = False,
      default=None,
      verbose_name=_("Дата записи")
    )

    time = models.TimeField(
      null=True,
      default=None,
      verbose_name=_("Время записи")
    )


    typepr = models.CharField(
      max_length=9,
      choices=TYPE_PRIEM,
      default=None,
      blank=False,
      null=True,
      verbose_name=_("Тип приема")
    )

    city = models.CharField(
      max_length=30,
      choices=CITIES,
      default=None,
      null=True,
      verbose_name=_("Город")
    )


    def __str__(self):
        return f'{self.lastname} {self.firstname[0]}., {self.typepr}'

    class Meta:
        unique_together = ('date', 'time', 'city')
        verbose_name = _("Запись")
        verbose_name_plural = _("Записи")