# Generated by Django 4.2.19 on 2025-04-01 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_orderlineitem_rename_created_at_order_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.CharField(default='27C5CDAC250749DBAE7894997FFFCD54', editable=False, max_length=32),
        ),
    ]
