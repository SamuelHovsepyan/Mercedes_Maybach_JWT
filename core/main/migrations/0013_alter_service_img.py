# Generated by Django 5.0.7 on 2024-09-01 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_rename_icon_service_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='img',
            field=models.ImageField(upload_to='', verbose_name='service img'),
        ),
    ]
