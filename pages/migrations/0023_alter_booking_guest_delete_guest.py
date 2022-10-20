# Generated by Django 4.1.2 on 2022-10-14 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0022_guests_alter_booking_guest_alter_booking_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='guest',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='pages.guests'),
        ),
        migrations.DeleteModel(
            name='Guest',
        ),
    ]