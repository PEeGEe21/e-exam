# Generated by Django 3.1.6 on 2021-05-11 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0031_auto_20210511_1120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='birth',
        ),
    ]