# Generated by Django 4.0.4 on 2022-05-09 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAuthModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=512)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.FloatField(max_length=11)),
                ('password', models.CharField(max_length=512)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('push_token', models.CharField(max_length=1024)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
