# Generated by Django 4.1.3 on 2023-03-28 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Daily_Records',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('l_date', models.DateField(auto_now_add=True)),
                ('login_time', models.TimeField(blank=True, null=True)),
                ('logout_time', models.TimeField(blank=True, null=True)),
                ('assignments', models.CharField(max_length=200)),
            ],
        ),
    ]
