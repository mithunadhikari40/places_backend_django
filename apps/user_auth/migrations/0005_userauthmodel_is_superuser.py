# Generated by Django 4.0.4 on 2022-05-10 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0004_userauthmodel_last_login_alter_userauthmodel_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='userauthmodel',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
