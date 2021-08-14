# Generated by Django 3.2.6 on 2021-08-13 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0014_auto_20210812_0556'),
        ('financial', '0002_auto_20210813_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.project', to_field='project_name'),
        ),
    ]