# Generated by Django 3.1.6 on 2021-04-18 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0015_auto_20210415_1837'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='password',
            new_name='password1',
        ),
        migrations.AddField(
            model_name='teacher',
            name='password2',
            field=models.CharField(default='000000', max_length=20, verbose_name='Password'),
        ),
    ]
