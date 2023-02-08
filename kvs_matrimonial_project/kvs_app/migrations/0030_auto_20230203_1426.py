# Generated by Django 3.2.9 on 2023-02-03 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kvs_app', '0029_join_kvs_dob'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='extendedusermodel',
            options={'verbose_name_plural': 'Extended User Model'},
        ),
        migrations.AlterModelOptions(
            name='statecommitie',
            options={'verbose_name_plural': 'State Commitie'},
        ),
        migrations.AlterField(
            model_name='join_kvs',
            name='id_proof_no',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]