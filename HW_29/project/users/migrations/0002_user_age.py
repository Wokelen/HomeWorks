# Generated by Django 4.1.7 on 2023-03-21 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
