# Generated by Django 3.1.6 on 2021-02-26 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20210225_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='award',
            field=models.TextField(default=None, max_length=50),
        ),
    ]
