# Generated by Django 3.2.9 on 2023-01-30 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kvs_app', '0028_remove_join_kvs_staff_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='join_kvs',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]