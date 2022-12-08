# Generated by Django 4.1.3 on 2022-12-08 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopsketch', '0003_alter_product_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopsketch.product')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
