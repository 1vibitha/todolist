# Generated by Django 5.0.6 on 2024-06-22 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tasktitle', models.CharField(max_length=30)),
                ('taskdesc', models.TextField(max_length=30)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
