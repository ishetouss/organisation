# Generated by Django 2.2.1 on 2020-08-15 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20200816_0011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='program',
            old_name='full_name',
            new_name='title',
        ),
    ]
