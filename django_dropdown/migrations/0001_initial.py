# Generated by Django 4.1.2 on 2022-10-14 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_dropdown.car')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_dropdown.car')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_dropdown.model')),
            ],
        ),
    ]
