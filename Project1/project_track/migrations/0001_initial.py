# Generated by Django 3.0.3 on 2020-06-11 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('county', models.CharField(max_length=100)),
                ('facility', models.CharField(max_length=100)),
                ('email_confirmed', models.BooleanField(default=False)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('Facility_Name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('Type', models.CharField(max_length=20)),
                ('County', models.CharField(max_length=50)),
                ('Number_of_Beds', models.IntegerField(blank=True)),
                ('Address', models.CharField(blank=True, max_length=200)),
                ('City', models.CharField(blank=True, max_length=50)),
                ('State', models.CharField(blank=True, max_length=30)),
                ('Zipcode', models.IntegerField(blank=True)),
                ('Telephone', models.CharField(blank=True, max_length=20)),
                ('Fax', models.CharField(blank=True, max_length=20)),
                ('Admin', models.CharField(blank=True, max_length=50)),
                ('Admin_Email', models.CharField(blank=True, max_length=50)),
                ('Social_Worker', models.CharField(blank=True, max_length=50)),
                ('SW_Email', models.CharField(blank=True, max_length=50)),
                ('Markt_or_Admission', models.CharField(blank=True, max_length=50)),
                ('Markt_or_Admission_Email', models.CharField(blank=True, max_length=50)),
                ('Accept_New_Residents', models.CharField(blank=True, max_length=50)),
                ('Age_Limit', models.IntegerField(blank=True)),
                ('Memory_Care', models.CharField(blank=True, max_length=50)),
                ('Behavior_or_Psych_Unit', models.CharField(blank=True, max_length=50)),
                ('Payments', models.CharField(blank=True, max_length=20)),
                ('Accept_Quadriplegic_and_Paraplegic', models.CharField(blank=True, max_length=50)),
                ('Accept_Patients_with_Chemical_Dependence_History', models.CharField(blank=True, max_length=50)),
                ('Accept_Chemical_Dependence', models.CharField(blank=True, max_length=50)),
                ('Hearing_Impairment_Accommodation', models.CharField(blank=True, max_length=50)),
                ('Visual_Impairment_Accommodation', models.CharField(blank=True, max_length=50)),
                ('Wound_Care', models.CharField(blank=True, max_length=50)),
                ('Wander_Guard', models.CharField(blank=True, max_length=50)),
                ('VA_Contracts', models.CharField(blank=True, max_length=50)),
                ('Respite_Care', models.CharField(blank=True, max_length=50)),
                ('Coma', models.CharField(blank=True, max_length=50)),
                ('Bariatric_Care', models.CharField(blank=True, max_length=50)),
                ('IV_Therapy', models.CharField(blank=True, max_length=50)),
                ('Trach_Tube_or_Ventilator', models.CharField(blank=True, max_length=50)),
                ('Dialysis', models.CharField(blank=True, max_length=30)),
                ('Notes', models.CharField(blank=True, max_length=200)),
                ('Accept_COVID_Patients', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('Facility_Name', models.CharField(max_length=50)),
                ('County', models.CharField(max_length=50)),
                ('Timestamp', models.DateTimeField(auto_now=True, max_length=50)),
                ('As_of', models.DateField(auto_now_add=True, max_length=30)),
                ('Open_Female_Medicaid_Beds', models.IntegerField(blank=True)),
                ('Open_Male_Medicaid_Beds', models.IntegerField(blank=True)),
                ('Open_Female_Medicare_Beds', models.IntegerField(blank=True)),
                ('Open_Male_Medicare_Beds', models.IntegerField(blank=True)),
                ('Open_Female_Private_Pay_Beds', models.IntegerField(blank=True)),
                ('Open_Male_Private_Pay_Beds', models.IntegerField(blank=True)),
                ('Open_Female_Dementia_Beds', models.IntegerField(blank=True)),
                ('Open_Male_Dementia_Beds', models.IntegerField(blank=True)),
                ('Notes', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
