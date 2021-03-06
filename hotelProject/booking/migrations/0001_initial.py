# Generated by Django 4.0.5 on 2022-07-06 10:04

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in_date', models.DateTimeField(auto_now_add=True)),
                ('check_out_date', models.DateTimeField(auto_now_add=True)),
                ('nb_Adults', models.PositiveIntegerField(default=1, verbose_name='Adults')),
                ('nb_Children', models.PositiveIntegerField(default=0, verbose_name='Children')),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='CheckInVisitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('B', 'Booking'), ('R', 'Reception'), ('T', 'Telephon'), ('E', 'Email')], default='B', max_length=20)),
                ('booking_status', models.CharField(choices=[('A', 'Available'), ('B', 'Booked'), ('C1', 'Cancelled by user'), ('C2', 'Cancelled by Manager')], default='B', max_length=2)),
                ('From_date', models.DateTimeField(blank=True, null=True, verbose_name='From')),
                ('To_date', models.DateTimeField(blank=True, null=True, verbose_name='To')),
                ('nb_days', models.PositiveIntegerField(default=1, verbose_name='nb_days')),
                ('deadline_free_Cancelation', models.DateTimeField(blank=True, null=True)),
                ('_total_cost', models.DecimalField(decimal_places=3, max_digits=10)),
                ('_discounted_price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=29, null=True)),
                ('comment', models.TextField(max_length=250)),
                ('rate', models.PositiveIntegerField(default=3, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='RoomBooked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nb_Adults', models.PositiveIntegerField(default=1, verbose_name='Adults')),
                ('nb_Children', models.PositiveIntegerField(default=0, verbose_name='Children')),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='RoomVisitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Identity_card_type', models.CharField(choices=[('Passport', 'Passport'), ('National ID', 'national identity')], default='Passport', max_length=11)),
                ('passport_picture', models.ImageField(null=True, upload_to='_img/')),
                ('Identity_Card_number', models.CharField(max_length=20, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('nationality', django_countries.fields.CountryField(blank=True, default='Saudi Arabia', max_length=2)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceBooked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qte', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.roombooked')),
            ],
        ),
    ]
