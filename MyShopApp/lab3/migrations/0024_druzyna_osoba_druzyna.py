# Generated by Django 4.1.3 on 2022-11-02 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lab3', '0023_alter_osoba_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Druzyna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100)),
                ('kraj', models.CharField(max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='osoba',
            name='druzyna',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lab3.druzyna'),
        ),
    ]
