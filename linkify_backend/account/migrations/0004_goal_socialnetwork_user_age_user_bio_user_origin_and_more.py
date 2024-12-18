# Generated by Django 5.1.2 on 2024-11-13 10:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='SocialNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(unique=True)),
                ('media_type', models.CharField(choices=[('REDDIT', 'Reddit'), ('X', 'X'), ('TELEGRAM', 'Telegram'), ('INSTAGRAM', 'Instagram')], max_length=20)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='social_network_icons/')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(120)]),
        ),
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, max_length='1000', null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='origin',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='goals',
            field=models.ManyToManyField(related_name='users', to='account.goal'),
        ),
    ]
