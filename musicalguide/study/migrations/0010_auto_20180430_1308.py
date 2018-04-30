# Generated by Django 2.0.4 on 2018-04-30 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0009_auto_20180430_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='first_compared_to_friends',
            field=models.CharField(choices=[('1', '1 (much worse)'), ('2', '2 (a bit worse)'), ('3', '3 (about the same'), ('4', '4 (a bit better)'), ('5', '5 (much better)')], default='', max_length=2),
        ),
        migrations.AddField(
            model_name='participant',
            name='first_compared_to_self',
            field=models.CharField(choices=[('1', '1 (much worse)'), ('2', '2 (a bit worse)'), ('3', '3 (about the same'), ('4', '4 (a bit better)'), ('5', '5 (much better)')], default='', max_length=2),
        ),
        migrations.AddField(
            model_name='participant',
            name='second_compared_to_friends',
            field=models.CharField(choices=[('1', '1 (much worse)'), ('2', '2 (a bit worse)'), ('3', '3 (about the same'), ('4', '4 (a bit better)'), ('5', '5 (much better)')], default='', max_length=2),
        ),
        migrations.AddField(
            model_name='participant',
            name='second_compared_to_self',
            field=models.CharField(choices=[('1', '1 (much worse)'), ('2', '2 (a bit worse)'), ('3', '3 (about the same'), ('4', '4 (a bit better)'), ('5', '5 (much better)')], default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='participant',
            name='system_preferred',
            field=models.CharField(choices=[('0', 'First system'), ('1', 'Second system')], default='', max_length=2),
        ),
    ]