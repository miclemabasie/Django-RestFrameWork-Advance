# Generated by Django 4.0.10 on 2023-11-21 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_category_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='slud',
            new_name='slug',
        ),
    ]