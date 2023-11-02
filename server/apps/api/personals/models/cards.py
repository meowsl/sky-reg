from django.db import models
from django.utils.translation import gettext_lazy as _

class PatientsCards(models.Model):
  TYPE_SEX = [
    ('М', 'Мужской'),
    ('Ж', 'Женский')
  ]
  TYPE_IS = [
    ('Да', 'Да'),
    ('Нет', 'Нет')
  ]
  # Добавить id
  lastname = models.CharField(
    max_length=300,
    null=True,
    blank=False,
    verbose_name=_("Фамилия")
  )

  firstname = models.CharField(
    max_length=30,
    null=True,
    blank=False,
    verbose_name = _("Имя")
    )

  midname = models.CharField(
    max_length=30,
    null=True,
    blank=True,
    verbose_name = _("Отчество")
    )

  sex = models.CharField(
    choices=TYPE_SEX,
    max_length=1,
    blank=False,
    null=True,
    verbose_name=_("Пол")
  )

  birthday = models.DateField(
    null=True,
    blank=False,
    verbose_name=_("Дата рождения")
  )

  phone = models.CharField(
    max_length=16,
    null=True,
    blank=False,
    verbose_name=_("Номер телефона")
  )

  address_obl = models.CharField(
    max_length=70,
    blank=False,
    null=True,
    verbose_name=_("Область")
  )

  address_city = models.CharField(
    max_length=70,
    blank=False,
    null=True,
    verbose_name=_("Населенный пункт")
  )

  address_street = models.CharField(
    max_length=70,
    blank=False,
    null=True,
    verbose_name=_("Улица")
  )

  address_house = models.CharField(
    max_length=10,
    blank=False,
    null=True,
    verbose_name=_("Номер дома")
  )

  address_korpus = models.CharField(
    max_length=70,
    blank=True,
    null=True,
    verbose_name=_("Корпус")
  )

  address_flat = models.IntegerField(
    blank=True,
    null=True,
    verbose_name=_("Номер квартиры")
  )

  work_place = models.CharField(
    max_length=100,
    blank=True,
    null=True,
    verbose_name=_("Место работы")
  )

  work_position = models.CharField(
    max_length=100,
    blank=True,
    null=True,
    verbose_name=_("Должность")
  )

  is_dependent = models.CharField(
    choices = TYPE_IS,
    max_length=3,
    blank=True,
    null=False,
    verbose_name=_('Иждевенец')
  )

  def __str__(self):
      return f'{self.lastname} {self.firstname[0]}. {self.midname[0]}. , {self.address_city}'

  class Meta:
      verbose_name = _("Карточка пациента")
      verbose_name_plural = _("Карточки пациентов")