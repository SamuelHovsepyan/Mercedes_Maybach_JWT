# Generated by Django 5.0.7 on 2024-07-30 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='logo',
            name='name',
            field=models.CharField(blank=True, max_length=40, verbose_name='Name'),
        ),
    ]
