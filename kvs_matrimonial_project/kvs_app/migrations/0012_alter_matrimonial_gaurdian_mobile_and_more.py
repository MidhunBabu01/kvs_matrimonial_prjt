# Generated by Django 4.1 on 2022-08-30 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kvs_app', '0011_star_matrimonial_gaurdian_mobile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matrimonial',
            name='gaurdian_mobile',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='matrimonial',
            name='gaurdian_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
