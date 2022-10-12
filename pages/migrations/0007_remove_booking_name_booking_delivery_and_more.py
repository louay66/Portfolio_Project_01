# Generated by Django 4.1.2 on 2022-10-11 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_rename_article_prodact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='name',
        ),
        migrations.AddField(
            model_name='booking',
            name='delivery',
            field=models.DateField(null=True, verbose_name='date of delivery the prodact'),
        ),
        migrations.AddField(
            model_name='booking',
            name='first_name',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='last_name',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='prodact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.prodact'),
        ),
        migrations.AddField(
            model_name='booking',
            name='receipt',
            field=models.DateField(null=True, verbose_name='date of receipt the prodact'),
        ),
    ]
