# Generated by Django 2.2.12 on 2022-11-12 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Technician', '0008_booking_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
