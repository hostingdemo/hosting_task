# Generated by Django 3.2.4 on 2021-06-23 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_auto_20210623_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='class_name',
            field=models.CharField(choices=[('Class Nursery', 'Class Nursery'), ('Class LKG', 'Class LKG'), ('Class PRE KG', 'Class PRE KG'), ('Class UKG', 'Class UKG'), ('Class I', 'Class I'), ('Class II', 'Class II'), ('Class III', 'Class III'), ('Class IV', 'Class IV'), ('Class V', 'Class V'), ('Class VI', 'Class VI'), ('Class VII', 'Class VII'), ('Class VIII', 'Class VIII'), ('Class IX', 'Class IX'), ('Class X', 'Class X'), ('Class XI', 'Class XI'), ('Class XII', 'Class XII')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='admissionenquiry',
            name='class_name',
            field=models.CharField(choices=[('Class Nursery', 'Class Nursery'), ('Class LKG', 'Class LKG'), ('Class PRE KG', 'Class PRE KG'), ('Class UKG', 'Class UKG'), ('Class I', 'Class I'), ('Class II', 'Class II'), ('Class III', 'Class III'), ('Class IV', 'Class IV'), ('Class V', 'Class V'), ('Class VI', 'Class VI'), ('Class VII', 'Class VII'), ('Class VIII', 'Class VIII'), ('Class IX', 'Class IX'), ('Class X', 'Class X'), ('Class XI', 'Class XI'), ('Class XII', 'Class XII')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='fees',
            name='frequency',
            field=models.CharField(choices=[('1', 'Monthly'), ('4', 'Quarterly'), ('6', 'Half yearly'), ('12', 'Annually')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='boarding',
            field=models.CharField(choices=[('1', 'Day school'), ('2', 'Day cum boarding school'), ('3', 'Play school')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='gender',
            field=models.CharField(choices=[('1', 'Coed'), ('2', 'Boys'), ('3', 'Girls')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='school_type',
            field=models.CharField(choices=[('1', 'Public School'), ('2', 'Private School'), ('3', 'Trust'), ('4', 'Society'), ('5', 'Municipal School'), ('6', 'Government School'), ('7', 'State Government School')], max_length=50, null=True),
        ),
    ]
