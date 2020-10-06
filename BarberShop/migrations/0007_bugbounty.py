# Generated by Django 3.1 on 2020-10-01 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BarberShop', '0006_auto_20200824_2301'),
    ]

    operations = [
        migrations.CreateModel(
            name='BugBounty',
            fields=[
                ('bug_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=255)),
                ('solved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
