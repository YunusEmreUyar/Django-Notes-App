# Generated by Django 3.2.7 on 2021-09-12 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_alter_profile_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='deadline',
        ),
    ]
