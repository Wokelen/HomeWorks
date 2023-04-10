# Generated by Django 4.1.7 on 2023-04-09 15:14

from django.db import migrations, models
import django.utils.timezone
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birth_date',
            field=models.DateField(default=django.utils.timezone.now, validators=[users.validators.check_birth_date]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True, validators=[users.validators.check_email]),
        ),
    ]