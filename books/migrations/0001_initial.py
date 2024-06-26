# Generated by Django 5.0.6 on 2024-05-18 09:11

import books.models
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('isbn', models.CharField(max_length=13, validators=[books.models.validate_isbn])),
                ('published_date', models.DateField()),
                ('stock', models.PositiveIntegerField()),
                ('genre', models.CharField(max_length=200)),
            ],
        ),
    ]
