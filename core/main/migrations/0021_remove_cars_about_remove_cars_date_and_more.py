# Generated by Django 5.0.7 on 2024-09-01 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_remove_cars_description_remove_cars_make_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cars',
            name='about',
        ),
        migrations.RemoveField(
            model_name='cars',
            name='date',
        ),
        migrations.RemoveField(
            model_name='cars',
            name='horsepower',
        ),
        migrations.RemoveField(
            model_name='cars',
            name='name',
        ),
        migrations.RemoveField(
            model_name='cars',
            name='price',
        ),
        migrations.RemoveField(
            model_name='cars',
            name='running',
        ),
        migrations.RemoveField(
            model_name='cars',
            name='transmission',
        ),
        migrations.RemoveField(
            model_name='cars',
            name='year',
        ),
    ]
