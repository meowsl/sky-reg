from django.db import models
from django.utils.translation import gettext_lazy as _

class Cabinets(models.Model):

    class City(models.IntegerChoices):
        ROSTOV = 1, _("Ростов-на-Дону")
        KRASNODAR = 2, _("Краснодар")
        SOCHI = 3, _("Сочи")

    CITY_CHOICES = {
        City.ROSTOV: _("Ростов-на-Дону"),
        City.KRASNODAR: _("Краснодар"),
        City.SOCHI: _("Сочи"),
    }

    city = models.PositiveIntegerField(
        choices=City.choices,
        blank=False,
        null=True,
        verbose_name=_("Город")
    )

    num = models.IntegerField(
        blank=False,
        null=True,
        verbose_name=_("Номер кабинета")
    )

    def get_city_display(self):
        return self.CITY_CHOICES.get(self.city, '')

    def __str__(self):
        return f'г. {self.get_city_display()}, кабинет №{self.num}'

    class Meta:
        verbose_name=_("Кабинет")
        verbose_name_plural=_("Кабинеты")