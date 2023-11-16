from django.db import models
from django.utils.translation import gettext_lazy as _

class Applications(models.Model):
    TYPE_PRIEM =[
      ('Первичный', 'Первичный'),
      ('Вторичный', 'Вторичный'),
      ('Обучение', 'Обучение')
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

    middlename = models.CharField(
      max_length=30,
      blank=True,
      verbose_name=_("Отчество")
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
      verbose_name=_("Дата обращения")
    )

    typepr = models.CharField(
      max_length=9,
      choices=TYPE_PRIEM,
      default=None,
      blank=False,
      null=True,
      verbose_name=_("Тип приема")
    )

    def __str__(self):
        return f'{self.last_name} {self.first_name[0]}. {self.middle_name[0]}. , {self.type_priem}'

    class Meta:
        verbose_name = _("Заявка")
        verbose_name_plural = _("Заявки")