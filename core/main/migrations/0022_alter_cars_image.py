# Generated by Django 5.0.7 on 2024-09-01 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_remove_cars_about_remove_cars_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='image',
            field=models.ImageField(upload_to='cars', verbose_name='Car image'),
        ),
    ]
