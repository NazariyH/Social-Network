# Generated by Django 5.1.2 on 2024-11-14 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_rename_heshstags_user_heshtags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='heshtags',
            new_name='hashtags',
        ),
    ]