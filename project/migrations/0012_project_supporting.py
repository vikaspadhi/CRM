# Generated by Django 3.2.6 on 2021-08-10 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_project_assigned_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='supporting',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=50, null=True),
        ),
    ]