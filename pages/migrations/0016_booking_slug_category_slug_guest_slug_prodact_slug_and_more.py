# Generated by Django 4.1.2 on 2022-10-14 10:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='slug',
            field=models.SlugField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='guest',
            name='slug',
            field=models.SlugField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='prodact',
            name='slug',
            field=models.SlugField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='guest',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
