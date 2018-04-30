# Generated by Django 2.0.4 on 2018-04-30 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0008_auto_20180430_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='second_system_bad',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='participant',
            name='second_system_estimated_time',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='participant',
            name='second_system_good',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='participant',
            name='second_system_impression',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='participant',
            name='second_system_play_again',
            field=models.CharField(choices=[('y', 'yes'), ('n', 'no')], default='', max_length=3),
        ),
        migrations.AddField(
            model_name='participant',
            name='second_system_rating',
            field=models.CharField(choices=[('1', '1 (not enjoyable at all)'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5 (very enjoyable)')], default='', max_length=2),
        ),
        migrations.AddField(
            model_name='participant',
            name='second_system_suggestions',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='participant',
            name='system_preferred',
            field=models.CharField(choices=[(0, 'First system'), (1, 'Second system')], default='', max_length=2),
        ),
        migrations.AddField(
            model_name='participant',
            name='why_system_preferred',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='participant',
            name='first_system_rating',
            field=models.CharField(choices=[('1', '1 (not enjoyable at all)'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5 (very enjoyable)')], default='', max_length=2),
        ),
    ]
