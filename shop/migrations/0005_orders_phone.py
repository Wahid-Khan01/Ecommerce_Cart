# Generated by Django 5.0.1 on 2024-02-13 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_orders_alter_contact_desc_alter_contact_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.CharField(default='', max_length=12),
        ),
    ]
