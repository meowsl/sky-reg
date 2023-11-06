from django.db import models
from django.utils.translation import gettext_lazy as _

class Applications(models.Model):
    TYPE_PRIEM =[
      ('Первичный', 'Первичный'),
      ('Вторичный', 'Вторичный'),
      ('Обучение', 'Обучение')
    ]

    last_name = models.CharField(
      max_length=30,
      blank=False,
      verbose_name=_("Фамилия")
    )

    first_name = models.CharField(
      max_length=30,
      blank=False,
      verbose_name=_("Имя")
    )

    middle_name = models.CharField(
      max_length=30,
      blank=False,
      verbose_name=_("Отчество")
    )

    phone = models.CharField(
      max_length=16,
      null=True,
      blank=False,
      verbose_name=_("Номер телефона")
    )

    date_application = models.DateField(
      blank = False,
      default=None,
      verbose_name=_("Дата обращения")
    )

    type_priem = models.CharField(
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