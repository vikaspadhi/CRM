# Generated by Django 3.2.6 on 2021-08-10 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20210810_1230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='balance',
        ),
    ]
