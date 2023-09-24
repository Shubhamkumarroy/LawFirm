# Generated by Django 4.2.5 on 2023-09-24 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprojectapp', '0011_advocate_advocatecatagory_alter_typelawer_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advocate',
            name='experience',
            field=models.CharField(default='N/A', max_length=255),
        ),
        migrations.AlterField(
            model_name='advocate',
            name='image_url',
            field=models.URLField(default='https://example.com/default-image.jpg'),
        ),
        migrations.AlterField(
            model_name='advocate',
            name='location',
            field=models.CharField(default='N/A', max_length=255),
        ),
        migrations.AlterField(
            model_name='advocate',
            name='name',
            field=models.CharField(default='N/A', max_length=255),
        ),
        migrations.AlterField(
            model_name='advocate',
            name='rating',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AlterField(
            model_name='advocate',
            name='type',
            field=models.CharField(default='Other', max_length=100),
        ),
        migrations.AlterField(
            model_name='advocatecatagory',
            name='cat',
            field=models.TextField(default='N/A'),
        ),
    ]
