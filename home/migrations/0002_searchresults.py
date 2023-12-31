# Generated by Django 4.2.2 on 2023-07-03 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('active_ingredient', models.CharField(max_length=255)),
                ('alcohol_warning', models.TextField()),
                ('breastfeeding_warning', models.TextField()),
                ('pregnancy_warning', models.TextField()),
                ('manufacturer', models.CharField(max_length=255)),
            ],
        ),
    ]
