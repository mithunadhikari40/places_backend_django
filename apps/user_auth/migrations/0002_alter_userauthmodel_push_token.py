# Generated by Django 4.0.4 on 2022-05-09 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userauthmodel',
            name='push_token',
            field=models.CharField(max_length=1024, null=True),
        ),
    ]
