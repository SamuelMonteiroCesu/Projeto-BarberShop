# Generated by Django 3.1 on 2020-11-27 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BarberShop', '0017_dayoff_professional'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='total',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
