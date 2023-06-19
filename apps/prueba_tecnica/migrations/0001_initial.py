# Generated by Django 4.0 on 2023-06-19 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicion',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('fecha', models.DateTimeField()),
                ('sensor', models.CharField(max_length=50)),
                ('medicion', models.DecimalField(decimal_places=10, max_digits=19)),
                ('estado', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Medición',
                'verbose_name_plural': 'Mediciones',
            },
        ),
    ]