# Generated by Django 3.1.6 on 2021-05-31 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0050_grade_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='grade',
            field=models.CharField(default='', max_length=20, verbose_name='score'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='score',
            field=models.IntegerField(),
        ),
    ]
