# Generated by Django 3.2.8 on 2022-11-25 16:40

from django.db import migrations, models
import list_film.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListFilm',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('coverImage', models.CharField(max_length=200)),
                ('coverImageH', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=100, verbose_name=list_film.models.TopicFilm)),
                ('description', models.TextField()),
                ('slug', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='TopicFilm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('_id', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=200)),
                ('slug', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=100)),
                ('itemType', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
