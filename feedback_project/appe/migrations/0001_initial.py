# Generated by Django 3.0.7 on 2020-06-29 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='feddback_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rateing', models.FloatField()),
                ('feedback', models.TextField(max_length=200)),
                ('date', models.DateField(max_length=100)),
            ],
        ),
    ]
