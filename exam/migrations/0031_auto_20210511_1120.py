# Generated by Django 3.1.6 on 2021-05-11 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0030_auto_20210511_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='dept',
            field=models.CharField(choices=[('Mathematics', 'Mathematics'), ('Computer Science', 'Computer Science'), ('BioChemistry', 'BioChemistry'), ('Accounting', 'Accounting'), ('Economics', 'Economics'), ('History', 'History'), ('Microbiology', 'Microbiology'), ('Mass Commuication', 'Mass Commuication'), ('International Relations', 'International Relations'), ('Criminology', 'Criminology'), ('Language and Linguistics', 'Language and Linguistics')], default=None, max_length=100, verbose_name='Department'),
        ),
    ]
