# Generated by Django 3.2.5 on 2021-10-06 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
