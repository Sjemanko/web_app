# Generated by Django 4.1.3 on 2022-12-01 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopsketch', '0002_alter_product_product_gender'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['id']},
        ),
    ]
