# Generated by Django 4.1.3 on 2022-12-01 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopsketch', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_gender',
            field=models.CharField(choices=[('ME', 'Male'), ('FE', 'Female')], default=('ME', 'Male'), max_length=2),
        ),
    ]