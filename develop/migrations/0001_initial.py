# Generated by Django 4.0.4 on 2022-08-14 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('caption', models.CharField(max_length=2000)),
                ('image', models.ImageField(upload_to='images')),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='floor_in_building', to='develop.building', verbose_name='building')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('floor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='room_on_floor', to='develop.floor', verbose_name='floor')),
            ],
        ),
    ]