# Generated by Django 2.2.5 on 2019-12-27 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='author',
            field=models.ForeignKey(blank=True, on_delete='models.CASCADE', to='taskmanager_app.User'),
        ),
    ]
