# Generated by Django 3.0.3 on 2020-05-25 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.CharField(blank=True, max_length=30, null=True)),
                ('female_medicaid', models.SmallIntegerField()),
                ('male_medicaid', models.SmallIntegerField(blank=True, null=True)),
                ('female_medicare', models.SmallIntegerField(blank=True, null=True)),
                ('male_medicare', models.SmallIntegerField(blank=True, null=True)),
                ('female_private', models.SmallIntegerField(blank=True, null=True)),
                ('male_private', models.SmallIntegerField(blank=True, null=True)),
                ('female_dementia', models.SmallIntegerField(blank=True, null=True)),
                ('male_dementia', models.SmallIntegerField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'facility',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PivotFacility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=10)),
                ('medicaid', models.SmallIntegerField()),
                ('medicare', models.SmallIntegerField(blank=True, null=True)),
                ('private', models.SmallIntegerField(blank=True, null=True)),
                ('dementia', models.SmallIntegerField(blank=True, null=True)),
            ],
        ),
    ]
