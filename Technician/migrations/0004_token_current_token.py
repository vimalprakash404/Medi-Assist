# Generated by Django 2.2.12 on 2022-11-06 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Technician', '0003_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='current_token',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
