# Generated by Django 5.0.6 on 2024-05-18 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_alter_member_debt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]