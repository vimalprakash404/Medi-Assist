# Generated by Django 2.2.12 on 2022-11-12 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Technician', '0014_remove_booking_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(default='pending', max_length=50),
        ),
    ]
