# Generated by Django 2.2.5 on 2019-12-27 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager_app', '0002_auto_20191227_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='author',
            field=models.ForeignKey(blank=True, default=False, on_delete='models.CASCADE', to='taskmanager_app.User'),
        ),
    ]