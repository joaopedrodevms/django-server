# Generated by Django 5.1.6 on 2025-02-06 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('nickname', models.CharField(default='', max_length=100)),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
