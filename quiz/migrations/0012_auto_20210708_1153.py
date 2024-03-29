# Generated by Django 3.2.4 on 2021-07-08 05:53

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0011_alter_question_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='question_number',
        ),
        migrations.RemoveField(
            model_name='course',
            name='total_marks',
        ),
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Option1', 'Вариант 1'), ('Option2', 'Вариант 2'), ('Option3', 'Вариант 3'), ('Option4', 'Вариант 4'), ('Option5', 'Вариант 5'), ('Picture1', 'Рисунок 1'), ('Picture2', 'Рисунок 2'), ('Picture3', 'Рисунок 3'), ('Picture4', 'Рисунок 4'), ('Picture5', 'Рисунок 5'), ('Entry_answer', 'Вводимый ответ')], default=False, max_length=200),
        ),
    ]
