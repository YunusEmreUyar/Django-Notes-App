# Generated by Django 3.2.7 on 2021-09-12 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0009_alter_notebook_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='is_public',
        ),
        migrations.AlterField(
            model_name='note',
            name='color',
            field=models.CharField(choices=[('blue', 'Blue'), ('red', 'Red'), ('green', 'DarkOliveGreen'), ('yellow', 'Gold'), ('CadetBlue', 'CadetBlue'), ('Lavender', 'Lavender'), ('LightBlue', 'LightBlue')], default='yellow', max_length=30),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='color',
            field=models.CharField(choices=[('blue', 'Blue'), ('red', 'Red'), ('green', 'DarkOliveGreen'), ('yellow', 'Gold'), ('CadetBlue', 'CadetBlue'), ('Lavender', 'Lavender'), ('LightBlue', 'LightBlue')], default='Lavender', max_length=30),
        ),
    ]
