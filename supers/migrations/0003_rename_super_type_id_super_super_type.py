# Generated by Django 4.0.3 on 2022-04-04 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supers', '0002_rename_super_type_super_super_type_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='super',
            old_name='super_type_id',
            new_name='super_type',
        ),
    ]
