# Generated by Django 3.2.9 on 2023-01-25 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kvs_app', '0022_sex_choices_alter_join_kvs_sex'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='join_kvs',
            name='taluk',
        ),
    ]
