# Generated by Django 3.1.6 on 2021-05-28 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecturers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='coverimage',
            field=models.ImageField(default='default.png', upload_to='cover_pics'),
        ),
    ]
