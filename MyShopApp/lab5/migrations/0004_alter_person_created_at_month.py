# Generated by Django 4.1.3 on 2022-12-08 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab5', '0003_person_team_remove_osoba_druzyna_delete_druzyna_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='created_at_month',
            field=models.IntegerField(default=12),
        ),
    ]