# Generated by Django 5.0.6 on 2024-06-23 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_task_tasks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='taskdesc',
            field=models.TextField(),
        ),
    ]