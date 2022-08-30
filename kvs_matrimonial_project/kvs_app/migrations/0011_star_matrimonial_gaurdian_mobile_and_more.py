# Generated by Django 4.1 on 2022-08-30 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kvs_app', '0010_matrimonial_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='matrimonial',
            name='gaurdian_mobile',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='matrimonial',
            name='gaurdian_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='matrimonial',
            name='marital_status',
            field=models.CharField(choices=[('Un Married', 'Un Married'), ('Second Marriage', 'Second Marriage'), ('Divorced', 'Divorced'), ('Widow', 'Widow')], max_length=25),
        ),
        migrations.AddField(
            model_name='matrimonial',
            name='star',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kvs_app.star'),
        ),
    ]
