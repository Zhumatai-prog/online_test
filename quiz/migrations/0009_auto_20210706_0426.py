# Generated by Django 3.2.4 on 2021-07-06 04:26

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_auto_20210628_0148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='marks',
        ),
        migrations.AddField(
            model_name='question',
            name='entry',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='entry_answer',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='option5',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='picture1',
            field=models.ImageField(blank=True, null=True, upload_to='static/questions-picture'),
        ),
        migrations.AddField(
            model_name='question',
            name='picture2',
            field=models.ImageField(blank=True, null=True, upload_to='static/questions-picture'),
        ),
        migrations.AddField(
            model_name='question',
            name='picture3',
            field=models.ImageField(blank=True, null=True, upload_to='static/questions-picture'),
        ),
        migrations.AddField(
            model_name='question',
            name='picture4',
            field=models.ImageField(blank=True, null=True, upload_to='static/questions-picture'),
        ),
        migrations.AddField(
            model_name='question',
            name='picture5',
            field=models.ImageField(blank=True, null=True, upload_to='static/questions-picture'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Option1', 'Option1'), ('Option2', 'Option2'), ('Option3', 'Option3'), ('Option4', 'Option4'), ('Option5', 'Option5'), ('Picture1', 'Picture1'), ('Picture2', 'Picture2'), ('Picture3', 'Picture3'), ('Picture4', 'Picture4'), ('Picture5', 'Picture5'), ('Entry_answer', 'Entry_answer')], default=False, max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='course',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='quiz.course'),
        ),
        migrations.AlterField(
            model_name='question',
            name='option1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='option2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='option3',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='option4',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]