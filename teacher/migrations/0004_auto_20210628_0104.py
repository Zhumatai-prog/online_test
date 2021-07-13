# Generated by Django 3.2.4 on 2021-06-28 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_alter_teacher_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='address',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='profile_pic',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='salary',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='status',
        ),
        migrations.AddField(
            model_name='teacher',
            name='email',
            field=models.EmailField(default=False, max_length=50),
        ),
    ]
