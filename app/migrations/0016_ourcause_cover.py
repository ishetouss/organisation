# Generated by Django 2.2.1 on 2020-08-10 10:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20200802_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourcause',
            name='cover',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/ibikorwa'),
            preserve_default=False,
        ),
    ]
