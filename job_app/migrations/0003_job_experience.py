# Generated by Django 4.2.5 on 2024-04-22 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_app', '0002_job_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='experience',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
