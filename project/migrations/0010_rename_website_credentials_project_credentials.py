# Generated by Django 3.2.6 on 2021-08-10 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_project_website_credentials'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='website_credentials',
            new_name='credentials',
        ),
    ]
