# Generated by Django 4.2.20 on 2025-04-16 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_alter_order_order_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.CharField(default='59A4F239465640FA8C4C4E05', editable=False, max_length=24, unique=True),
        ),
    ]
