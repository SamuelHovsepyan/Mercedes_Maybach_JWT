# Generated by Django 5.0.7 on 2024-09-01 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_alter_sign_image1_alter_sign_image2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car2',
            name='image',
            field=models.ImageField(upload_to='brands/'),
        ),
    ]
