# Generated by Django 3.2.6 on 2021-08-12 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0013_project_status_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='project_start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
