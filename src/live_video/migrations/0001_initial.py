# Generated by Django 3.2.8 on 2022-11-24 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LiveVideo',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=300)),
                ('slug', models.CharField(max_length=200)),
                ('durationStr', models.CharField(max_length=100)),
                ('coverImage', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
