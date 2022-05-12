# Generated by Django 4.0.4 on 2022-05-12 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSavedPlacesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=512)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.CharField(max_length=1024)),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=512)),
                ('monument', models.CharField(max_length=100)),
                ('latitude', models.FloatField(max_length=10)),
                ('longitude', models.FloatField(max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]