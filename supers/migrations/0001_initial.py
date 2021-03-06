# Generated by Django 4.0.3 on 2022-04-04 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('super_types', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Super',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('alter_ego', models.CharField(max_length=40)),
                ('primary_ability', models.CharField(max_length=40)),
                ('secondary_ability', models.CharField(max_length=40)),
                ('catchphrase', models.CharField(max_length=255)),
                ('super_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='super_types.supertype')),
            ],
        ),
    ]
