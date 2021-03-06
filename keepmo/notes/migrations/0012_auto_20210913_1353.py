# Generated by Django 3.2.7 on 2021-09-13 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0011_auto_20210912_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='color',
            field=models.CharField(choices=[('blue', 'Blue'), ('red', 'Red'), ('#cfc', 'DarkOliveGreen'), ('yellow', 'Gold'), ('CadetBlue', 'CadetBlue'), ('Lavender', 'Lavender'), ('LightBlue', 'LightBlue'), ('BurlyWood', 'BurlyWood'), ('BlueViolet', 'BlueViolet'), ('Cornsilk', 'Cornsilk'), ('IndianRed ', 'IndianRed '), ('LightGreen', 'LightGreen'), ('LightSlateGray', 'LightSlateGray'), ('PaleGoldenRod', 'PaleGoldenRod')], default='yellow', max_length=30),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='color',
            field=models.CharField(choices=[('blue', 'Blue'), ('red', 'DarkRed'), ('#cfc', 'DarkOliveGreen'), ('yellow', 'Gold'), ('CadetBlue', 'CadetBlue'), ('Lavender', 'Lavender'), ('LightBlue', 'LightBlue'), ('BurlyWood', 'BurlyWood'), ('BlueViolet', 'BlueViolet'), ('Cornsilk', 'Cornsilk'), ('IndianRed ', 'IndianRed '), ('LightGreen', 'LightGreen'), ('LightSlateGray', 'LightSlateGray'), ('PaleGoldenRod', 'PaleGoldenRod')], default='Lavender', max_length=30),
        ),
    ]
