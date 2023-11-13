# Generated by Django 3.2.22 on 2023-11-13 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skyreg', '0010_alter_krdschedule_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='SCHSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=150, null=True, verbose_name='Данные клиента')),
                ('date', models.DateField(default=None, verbose_name='Дата записи ')),
                ('typePriem', models.PositiveIntegerField(choices=[(1, 'Первичный'), (2, 'Вторичный'), (3, 'Обучение')], null=True, verbose_name='Тип приема')),
                ('cabinet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='skyreg.schcabinets', verbose_name='Кабинет')),
            ],
            options={
                'verbose_name': 'Расписание, Краснодар',
                'verbose_name_plural': 'Расписание, Краснодар',
            },
        ),
        migrations.CreateModel(
            name='RNDSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=150, null=True, verbose_name='Данные клиента')),
                ('date', models.DateField(default=None, verbose_name='Дата записи ')),
                ('typePriem', models.PositiveIntegerField(choices=[(1, 'Первичный'), (2, 'Вторичный'), (3, 'Обучение')], null=True, verbose_name='Тип приема')),
                ('cabinet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='skyreg.rndcabinets', verbose_name='Кабинет')),
            ],
            options={
                'verbose_name': 'Расписание, Краснодар',
                'verbose_name_plural': 'Расписание, Краснодар',
            },
        ),
    ]
