# Generated by Django 2.2.6 on 2019-11-21 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_tasks_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='color',
            field=models.CharField(default='#121212', max_length=255),
        ),
    ]
