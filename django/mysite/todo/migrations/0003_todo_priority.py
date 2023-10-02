# Generated by Django 4.2.4 on 2023-08-22 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='priority',
            field=models.CharField(blank=True, choices=[('優先度高', '!'), ('優先度中', '△'), ('優先度低', '⚪︎')], max_length=5),
        ),
    ]