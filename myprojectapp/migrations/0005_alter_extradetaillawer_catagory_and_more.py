# Generated by Django 4.2.5 on 2023-09-22 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprojectapp', '0004_remove_extradetaillawer_laweruser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extradetaillawer',
            name='catagory',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AlterField(
            model_name='extradetaillawer',
            name='contact',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AlterField(
            model_name='extradetaillawer',
            name='country',
            field=models.CharField(default='N/A', max_length=100),
        ),
    ]
