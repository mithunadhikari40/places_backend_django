# Generated by Django 4.0.4 on 2022-05-12 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersavedplacesmodel',
            name='deleted_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='usersavedplacesmodel',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='images/'),
        ),
    ]