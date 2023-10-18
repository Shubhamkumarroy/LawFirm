# Generated by Django 4.2.5 on 2023-09-25 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprojectapp', '0013_advocatecatagoryfin_advocatefin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aribitration_mediator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('experience', models.CharField(blank=True, max_length=255, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('practice_areas', models.TextField(blank=True, null=True)),
                ('language', models.CharField(blank=True, max_length=255, null=True)),
                ('photo_url', models.URLField(blank=True, null=True)),
                ('contact_link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]