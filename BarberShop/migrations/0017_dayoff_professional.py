# Generated by Django 3.1 on 2020-11-26 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BarberShop', '0016_dayoff'),
    ]

    operations = [
        migrations.AddField(
            model_name='dayoff',
            name='professional',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='BarberShop.authuser'),
        ),
    ]
