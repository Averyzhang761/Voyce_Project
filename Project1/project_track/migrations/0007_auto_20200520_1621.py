# Generated by Django 3.0.6 on 2020-05-20 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_track', '0006_auto_20200517_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_city',
            field=models.CharField(default='Saint Louis', max_length=60),
        ),
        migrations.AddField(
            model_name='user',
            name='user_facility',
            field=models.CharField(default='Facility 1', max_length=100),
        ),
    ]
