# Generated by Django 3.1.6 on 2021-06-01 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecturers', '0002_profile_coverimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='coverimage',
            field=models.ImageField(default='help-stand.jpg', upload_to='cover_pics'),
        ),
    ]