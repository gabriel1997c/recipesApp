# Generated by Django 3.0.2 on 2020-01-03 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='time',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
