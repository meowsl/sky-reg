# Generated by Django 3.2.22 on 2023-11-19 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personals', '0008_alter_applications_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='applications',
            unique_together={('date', 'time', 'city')},
        ),
    ]
