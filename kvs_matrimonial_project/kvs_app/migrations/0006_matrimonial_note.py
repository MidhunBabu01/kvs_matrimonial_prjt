# Generated by Django 4.1 on 2022-08-24 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kvs_app', '0005_alter_gender_choices_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='matrimonial',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
    ]
