# Generated by Django 3.1 on 2020-11-26 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BarberShop', '0015_schedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayOff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daydate', models.CharField(max_length=10)),
                ('reason', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]