# Generated by Django 5.0.7 on 2024-07-30 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_service_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='home_images', verbose_name='Car image')),
                ('name', models.CharField(max_length=100, verbose_name='Car name')),
                ('price', models.PositiveIntegerField(verbose_name='Car Price')),
                ('running', models.FloatField(verbose_name='Car running')),
                ('horsepower', models.PositiveIntegerField(verbose_name='Car horsepower')),
                ('transmission', models.CharField(choices=[('automatic', 'automatic'), ('manual', 'manual')], max_length=30, verbose_name='Transmission name')),
                ('about', models.TextField(verbose_name='Car about')),
                ('date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
