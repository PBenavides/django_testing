# Generated by Django 2.2 on 2020-01-07 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prueba_post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('action', models.CharField(max_length=250)),
                ('message', models.CharField(max_length=100)),
            ],
        ),
    ]
