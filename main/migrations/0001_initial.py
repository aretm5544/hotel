# Generated by Django 4.2.6 on 2023-11-15 17:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10)),
                ('price_per_night', models.DecimalField(decimal_places=2, max_digits=10)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.hotel')),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.roomtype')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in_date', models.DateField()),
                ('check_out_date', models.DateField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
