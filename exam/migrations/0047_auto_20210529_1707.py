# Generated by Django 3.1.6 on 2021-05-29 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0046_auto_20210529_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='course',
            field=models.CharField(default='', error_messages={'unique': 'The Course has already been created, Add Questions!'}, max_length=20, unique=True, verbose_name='Course'),
        ),
    ]