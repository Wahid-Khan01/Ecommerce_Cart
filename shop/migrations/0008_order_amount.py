# Generated by Django 5.0.1 on 2024-02-13 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_orderupdates'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.IntegerField(default=0, max_length=10000000),
        ),
    ]