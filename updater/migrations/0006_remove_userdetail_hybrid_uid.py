# Generated by Django 3.0.7 on 2021-01-15 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('updater', '0005_userdetail_hybrid_uid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetail',
            name='hybrid_uid',
        ),
    ]
