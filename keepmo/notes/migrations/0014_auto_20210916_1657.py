# Generated by Django 3.2.7 on 2021-09-16 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0013_auto_20210913_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(null=True, upload_to='profiles/'),
        ),
    ]
