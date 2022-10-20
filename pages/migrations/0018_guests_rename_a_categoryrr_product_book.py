# Generated by Django 4.1.2 on 2022-10-14 14:11

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_a_remove_booking_slug_remove_category_slug_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guests',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('first_name', models.CharField(max_length=10, null=True)),
                ('last_name', models.CharField(max_length=10, null=True)),
                ('phone_number', models.CharField(max_length=8, null=True)),
                ('delivery', models.DateField(null=True, verbose_name='date of delivery the prodact')),
                ('receipt', models.DateField(null=True, verbose_name='date of receipt the prodact')),
            ],
        ),
        migrations.RenameModel(
            old_name='A',
            new_name='Categoryrr',
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('image', models.ImageField(upload_to='%y/%m/%d')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.categoryrr')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('guest', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.guests')),
                ('prodact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='pages.product')),
            ],
        ),
    ]
