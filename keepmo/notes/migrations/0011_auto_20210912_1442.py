# Generated by Django 3.2.7 on 2021-09-12 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0010_auto_20210912_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='color',
            field=models.CharField(choices=[('blue', 'Blue'), ('red', 'Red'), ('green', 'DarkOliveGreen'), ('yellow', 'Gold'), ('CadetBlue', 'CadetBlue'), ('Lavender', 'Lavender'), ('LightBlue', 'LightBlue'), ('BurlyWood', 'BurlyWood'), ('BlueViolet', 'BlueViolet'), ('Cornsilk', 'Cornsilk'), ('IndianRed ', 'IndianRed '), ('LightGreen', 'LightGreen'), ('LightSlateGray', 'LightSlateGray'), ('PaleGoldenRod', 'PaleGoldenRod')], default='yellow', max_length=30),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='color',
            field=models.CharField(choices=[('blue', 'Blue'), ('red', 'DarkRed'), ('green', 'DarkOliveGreen'), ('yellow', 'Gold'), ('CadetBlue', 'CadetBlue'), ('Lavender', 'Lavender'), ('LightBlue', 'LightBlue'), ('BurlyWood', 'BurlyWood'), ('BlueViolet', 'BlueViolet'), ('Cornsilk', 'Cornsilk'), ('IndianRed ', 'IndianRed '), ('LightGreen', 'LightGreen'), ('LightSlateGray', 'LightSlateGray'), ('PaleGoldenRod', 'PaleGoldenRod')], default='Lavender', max_length=30),
        ),
    ]