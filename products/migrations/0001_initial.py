# Generated by Django 4.2.19 on 2025-04-15 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('category', models.PositiveSmallIntegerField(choices=[(1, 'Prints'), (2, 'Paintings'), (3, 'Clothing'), (4, 'Other')], default=4)),
                ('has_sizes', models.BooleanField(blank=True, default=False, null=True)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images/')),
            ],
        ),
    ]
