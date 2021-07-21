# Generated by Django 3.2.4 on 2021-06-23 12:50

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import newapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(choices=[('Class LKG', 'Class LKG'), ('Class PRE KG', 'Class PRE KG'), ('Class UKG', 'Class UKG'), ('Class I', 'Class I'), ('Class II', 'Class II'), ('Class III', 'Class III'), ('Class IV', 'Class IV'), ('Class V', 'Class V')], max_length=100, null=True)),
                ('session', models.CharField(max_length=50, null=True)),
                ('last_date', models.DateField(default=django.utils.timezone.now, null=True)),
                ('application_fees', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AdmissionEnquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=255, null=True)),
                ('phone', models.CharField(max_length=10, null=True)),
                ('class_name', models.CharField(choices=[('Class LKG', 'Class LKG'), ('Class PRE KG', 'Class PRE KG'), ('Class UKG', 'Class UKG'), ('Class I', 'Class I'), ('Class II', 'Class II'), ('Class III', 'Class III'), ('Class IV', 'Class IV'), ('Class V', 'Class V')], max_length=20, null=True)),
                ('message', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('year_established', models.IntegerField(validators=[django.core.validators.MinValueValidator(1900), newapp.models.max_value_current_year])),
                ('school_type', models.CharField(choices=[('Public School', 'Public School'), ('Private School', 'Private School'), ('Trust', 'Trust'), ('Society', 'Society'), ('Municipal School', 'Municipal School'), ('Government School', 'Government School'), ('State Government School', 'State Government School')], max_length=50, null=True)),
                ('boarding', models.CharField(choices=[('day', 'day'), ('night', 'night')], max_length=50, null=True)),
                ('gender', models.CharField(choices=[('Coed', 'Coed'), ('Boys', 'Boys'), ('Girls', 'Girls')], max_length=100, null=True)),
                ('grades_start', models.CharField(choices=[('Class LKG', 'Class LKG'), ('Class PRE KG', 'Class PRE KG'), ('Class UKG', 'Class UKG'), ('Class I', 'Class I'), ('Class II', 'Class II'), ('Class III', 'Class III'), ('Class IV', 'Class IV'), ('Class V', 'Class V')], max_length=50, null=True)),
                ('grades_end', models.CharField(choices=[('Class LKG', 'Class LKG'), ('Class PRE KG', 'Class PRE KG'), ('Class UKG', 'Class UKG'), ('Class I', 'Class I'), ('Class II', 'Class II'), ('Class III', 'Class III'), ('Class IV', 'Class IV'), ('Class V', 'Class V')], max_length=50, null=True)),
                ('management', models.CharField(max_length=50, null=True)),
                ('admission_period', models.DateField(default=django.utils.timezone.now, null=True)),
                ('language_of_instruction', models.CharField(max_length=50, null=True)),
                ('curriculum', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('phone_no', models.CharField(max_length=10, null=True)),
                ('chairman_name', models.CharField(max_length=100, null=True)),
                ('principal_name', models.CharField(max_length=100, null=True)),
                ('website', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Facilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sports_facilities', models.CharField(blank=True, max_length=1000, null=True)),
                ('education_facilities', models.CharField(blank=True, max_length=1000, null=True)),
                ('classroom_facilities', models.CharField(blank=True, max_length=1000, null=True)),
                ('visual_and_performing_art_facilities', models.CharField(blank=True, max_length=1000, null=True)),
                ('laboratories_facilities', models.CharField(blank=True, max_length=1000, null=True)),
                ('transport_facilities', models.CharField(blank=True, max_length=1000, null=True)),
                ('boarding_facilities', models.CharField(blank=True, max_length=1000, null=True)),
                ('accessibility_facilities', models.CharField(blank=True, max_length=1000, null=True)),
                ('digital_facilities', models.CharField(blank=True, max_length=1000, null=True)),
                ('safety_and_security_facilities', models.CharField(blank=True, max_length=1000, null=True)),
                ('food_and_catering_facilities', models.CharField(blank=True, max_length=1000, null=True)),
                ('medical_facility_facilities', models.CharField(blank=True, max_length=1000, null=True)),
                ('other_infra_facilities', models.CharField(blank=True, max_length=1000, null=True)),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='newapp.school')),
            ],
        ),
        migrations.CreateModel(
            name='AdmissionDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academic_year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1984), newapp.models.max_value_current_year])),
                ('admission_period', models.CharField(max_length=100, null=True)),
                ('fee_details', models.CharField(max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='newapp.school')),
            ],
        ),
    ]
