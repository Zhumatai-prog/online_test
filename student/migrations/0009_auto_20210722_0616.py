# Generated by Django 3.2.4 on 2021-07-22 00:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_alter_student_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dept',
            options={'verbose_name': 'Отдел', 'verbose_name_plural': 'Отдел'},
        ),
        migrations.AlterModelOptions(
            name='position',
            options={'verbose_name': 'Должность', 'verbose_name_plural': 'Должность'},
        ),
    ]
