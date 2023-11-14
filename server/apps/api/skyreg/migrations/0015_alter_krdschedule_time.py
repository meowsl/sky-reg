# Generated by Django 3.2.22 on 2023-11-14 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skyreg', '0014_alter_krdschedule_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='krdschedule',
            name='time',
            field=models.CharField(choices=[('10:00', '10:00'), ('10:30', '10:30'), ('11:00', '11:00'), ('11:30', '11:30'), ('12:00', '12:00'), ('12:30', '12:30'), ('13:00', '13:00'), ('13:30', '13:30'), ('14:00', '14:00'), ('14:30', '14:30'), ('15:00', '15:00'), ('15:30', '15:30'), ('16:00', '16:00'), ('16:30', '16:30'), ('17:00', '17:00'), ('17:30', '17:30'), ('18:00', '18:00'), ('18:30', '18:30')], max_length=5, null=True, verbose_name='Время'),
        ),
    ]
