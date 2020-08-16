# Generated by Django 2.2.1 on 2020-08-10 11:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_ourcause_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='cover',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/blog'),
            preserve_default=False,
        ),
    ]
