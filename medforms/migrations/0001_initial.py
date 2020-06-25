# Generated by Django 3.0.3 on 2020-03-07 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MedServiceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('med_text', models.TextField()),
                ('features', models.TextField(blank=True)),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
            ],
        ),
    ]
