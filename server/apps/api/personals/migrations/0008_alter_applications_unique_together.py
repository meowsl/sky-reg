# Generated by Django 3.2.22 on 2023-11-19 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personals', '0007_auto_20231119_1325'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='applications',
            unique_together={('date', 'time')},
        ),
    ]
