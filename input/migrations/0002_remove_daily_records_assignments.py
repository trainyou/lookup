# Generated by Django 4.1.3 on 2023-03-28 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='daily_records',
            name='assignments',
        ),
    ]
