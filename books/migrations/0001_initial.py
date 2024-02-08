# Generated by Django 5.0.2 on 2024-02-08 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Providers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('Phone_number', models.IntegerField()),
                ('Email', models.CharField(max_length=50, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Провайдер',
                'verbose_name_plural': 'Провайдеры',
            },
        ),
    ]
