# Generated by Django 4.2.19 on 2025-04-16 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_alter_order_order_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.CharField(default='5A84F8B89BA84C58872DDB66', editable=False, max_length=24, unique=True),
        ),
    ]
