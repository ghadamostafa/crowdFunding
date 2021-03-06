# Generated by Django 3.0.4 on 2020-08-13 01:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='featured_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='projects',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Featured_projects',
        ),
    ]
