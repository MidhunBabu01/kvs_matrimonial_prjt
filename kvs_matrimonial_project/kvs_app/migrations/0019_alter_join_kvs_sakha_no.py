# Generated by Django 4.1 on 2022-11-21 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kvs_app', '0018_auto_20220922_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='join_kvs',
            name='sakha_no',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
