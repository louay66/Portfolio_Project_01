# Generated by Django 4.1.2 on 2022-10-14 14:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0021_rename_prodact_booking_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('first_name', models.CharField(max_length=10, null=True)),
                ('last_name', models.CharField(max_length=10, null=True)),
                ('phone_number', models.CharField(max_length=8, null=True)),
                ('delivery', models.DateField(null=True, verbose_name='date of delivery the prodact')),
                ('receipt', models.DateField(null=True, verbose_name='date of receipt the prodact')),
            ],
        ),
        migrations.AlterField(
            model_name='booking',
            name='guest',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='pages.guest'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='booking', to='pages.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='pages.category'),
        ),
    ]