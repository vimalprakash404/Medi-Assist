# Generated by Django 2.2.12 on 2022-11-21 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Technician', '0018_auto_20221121_0424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='test',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Technician.booking'),
        ),
    ]
