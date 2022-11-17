# Generated by Django 4.1.3 on 2022-11-17 10:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lab5', '0003_person_team_remove_osoba_druzyna_delete_druzyna_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='owner',
            field=models.ForeignKey(null='true', on_delete=django.db.models.deletion.CASCADE, related_name='Person', to=settings.AUTH_USER_MODEL),
            preserve_default='true',
        ),
    ]
