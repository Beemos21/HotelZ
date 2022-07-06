# Generated by Django 4.0.5 on 2022-07-06 10:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import roomManager.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('currencyapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=20)),
                ('city_name_ar', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='HotelInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('name_ar', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('reg_number', models.CharField(max_length=10)),
                ('owner_name', models.CharField(max_length=255, null=True)),
                ('address', models.CharField(max_length=400)),
                ('state', models.CharField(max_length=25, null=True)),
                ('phone', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='roomManager.city')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('rfloor', models.IntegerField(default=1, null=True)),
                ('cover_image', models.ImageField(upload_to=roomManager.models.room_images_upload_path)),
                ('is_active', models.BooleanField(default=False)),
                ('featured', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('hotel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='roomManager.hotelinfo')),
            ],
        ),
        migrations.CreateModel(
            name='RoomService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.BooleanField()),
                ('free', models.BooleanField()),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='RoomStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomstatus', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'verbose_name_plural': 'Room Status',
            },
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(choices=[('Single room', 'Single room'), ('Twin room', 'Twin room'), ('Double room', 'Double room'), ('Triple room', 'Triple room'), ('Quad room', 'Quad room'), ('Double-Double room', 'Double-Double room'), ('Queen room', 'Queen room'), ('King room', 'Suite'), ('King room', 'Suite'), ('Presidential suite', 'Presidential suite'), ('Studio', 'Studio'), ('Connecting rooms', 'Connecting rooms'), ('Junior Suite', 'Junior Suite')], default='Twin room', max_length=20)),
                ('type_name_ar', models.CharField(choices=[('غرفه مفرده', 'غرفه مفرده'), ('غرفة توأم', 'غرفة توأم'), ('غرفة مزدوجة ', 'غرفة مزدوجة '), ('غرفه ثلاثيه', 'غرفه ثلاثيه'), ('غرفه رباعيه', 'غرفه رباعيه'), ('مزدوج مزدوجة ثنائية', 'مزدوج مزدوجة ثنائية'), ('غرفة الملكة', 'غرفة الملكة'), ('غرفة الملك', 'غرفة الملك'), ('جناح', 'جناح'), ('جناح الرئيس | الجناح الرئاسي', 'جناح الرئيس | الجناح الرئاسي'), ('الاستوديو', 'الاستوديو'), ('الغرف المتصلة', 'الغرف المتصلة'), ('جناح صغير', 'جناح صغير')], default='Twin room', max_length=30)),
                ('area', models.IntegerField(default=10)),
                ('bedType', models.CharField(choices=[('1 double bed', '1 double bed'), ('1 double bed and 1 Sofa', '1 double bed and 1 Sofa'), ('2 single beds', '2 single beds'), ('1 Sofa and 1 single bed', '1 Single Sofa Bed and 1 single bed'), ('king Bed', 'king Bed')], default='1 double bed', max_length=23)),
                ('bedType_ar', models.CharField(choices=[('سرير لفردين', 'سرير لفردين'), ('1 سرير لفردين و 1 سرير أريكة', '1 سرير لفردين 1 سرير أريكة'), ('2 سرير لفرد واحد', '2 سرير لفرد واحد'), ('1 سرير أريكة 1 سرير لفرد واحد', '1 سرير أريكة 1 سرير لفرد واحد'), (' سرير كبير لفردين', 'سرير كبير لفردين')], default='سرير لفردين ', max_length=30)),
                ('capacity', models.IntegerField(default=2)),
                ('cover_image', models.ImageField(upload_to=roomManager.models.room_images_upload_path)),
                ('price_per_day', models.DecimalField(decimal_places=3, max_digits=10)),
                ('description', models.CharField(max_length=50)),
                ('special_features', models.CharField(max_length=50)),
                ('description_ar', models.CharField(max_length=50)),
                ('special_features_ar', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('currency', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='currencyapp.currency')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('name_ar', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('description', models.TextField(max_length=250)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('currency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='currencyapp.currency')),
            ],
        ),
        migrations.CreateModel(
            name='RoomTypeDisplayImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_images', models.ImageField(upload_to=roomManager.models.room_display_images_upload_path)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('roomtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roomManager.roomtype')),
            ],
        ),
        migrations.AddField(
            model_name='roomtype',
            name='services',
            field=models.ManyToManyField(related_name='sevices', through='roomManager.RoomService', to='roomManager.service'),
        ),
        migrations.AddField(
            model_name='roomservice',
            name='roomtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roomManager.roomtype'),
        ),
        migrations.AddField(
            model_name='roomservice',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roomManager.service'),
        ),
        migrations.CreateModel(
            name='RoomDisplayImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_images', models.ImageField(upload_to=roomManager.models.room_display_images_upload_path)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roomManager.room')),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='room_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='roomManager.roomstatus'),
        ),
        migrations.AddField(
            model_name='room',
            name='rtype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='roomManager.roomtype'),
        ),
        migrations.CreateModel(
            name='HotelUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_default', models.BooleanField()),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roomManager.hotelinfo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='hotelinfo',
            name='user',
            field=models.ManyToManyField(related_name='users', through='roomManager.HotelUser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Availability_Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d1', models.CharField(default='0', max_length=2)),
                ('d2', models.CharField(default='0', max_length=2)),
                ('d3', models.CharField(default='0', max_length=2)),
                ('d4', models.CharField(default='0', max_length=2)),
                ('d5', models.CharField(default='0', max_length=2)),
                ('d6', models.CharField(default='0', max_length=2)),
                ('d7', models.CharField(default='0', max_length=2)),
                ('d8', models.CharField(default='0', max_length=2)),
                ('d9', models.CharField(default='0', max_length=2)),
                ('d10', models.CharField(default='0', max_length=2)),
                ('d11', models.CharField(default='0', max_length=2)),
                ('d12', models.CharField(default='0', max_length=2)),
                ('d13', models.CharField(default='0', max_length=2)),
                ('d14', models.CharField(default='0', max_length=2)),
                ('d15', models.CharField(default='0', max_length=2)),
                ('d16', models.CharField(default='0', max_length=2)),
                ('d17', models.CharField(default='0', max_length=2)),
                ('d18', models.CharField(default='0', max_length=2)),
                ('d19', models.CharField(default='0', max_length=2)),
                ('d20', models.CharField(default='0', max_length=2)),
                ('d21', models.CharField(default='0', max_length=2)),
                ('d22', models.CharField(default='0', max_length=2)),
                ('d23', models.CharField(default='0', max_length=2)),
                ('d24', models.CharField(default='0', max_length=2)),
                ('d25', models.CharField(default='0', max_length=2)),
                ('d26', models.CharField(default='0', max_length=2)),
                ('d27', models.CharField(default='0', max_length=2)),
                ('d28', models.CharField(default='0', max_length=2)),
                ('d29', models.CharField(default='0', max_length=2)),
                ('d30', models.CharField(default='0', max_length=2)),
                ('d31', models.CharField(default='0', max_length=2)),
                ('d32', models.CharField(default='0', max_length=2)),
                ('d33', models.CharField(default='0', max_length=2)),
                ('d34', models.CharField(default='0', max_length=2)),
                ('d35', models.CharField(default='0', max_length=2)),
                ('d36', models.CharField(default='0', max_length=2)),
                ('d37', models.CharField(default='0', max_length=2)),
                ('d38', models.CharField(default='0', max_length=2)),
                ('d39', models.CharField(default='0', max_length=2)),
                ('d40', models.CharField(default='0', max_length=2)),
                ('d41', models.CharField(default='0', max_length=2)),
                ('d42', models.CharField(default='0', max_length=2)),
                ('d43', models.CharField(default='0', max_length=2)),
                ('d44', models.CharField(default='0', max_length=2)),
                ('d45', models.CharField(default='0', max_length=2)),
                ('d46', models.CharField(default='0', max_length=2)),
                ('d47', models.CharField(default='0', max_length=2)),
                ('d48', models.CharField(default='0', max_length=2)),
                ('d49', models.CharField(default='0', max_length=2)),
                ('d50', models.CharField(default='0', max_length=2)),
                ('d51', models.CharField(default='0', max_length=2)),
                ('d52', models.CharField(default='0', max_length=2)),
                ('d53', models.CharField(default='0', max_length=2)),
                ('d54', models.CharField(default='0', max_length=2)),
                ('d55', models.CharField(default='0', max_length=2)),
                ('d56', models.CharField(default='0', max_length=2)),
                ('d57', models.CharField(default='0', max_length=2)),
                ('d58', models.CharField(default='0', max_length=2)),
                ('d59', models.CharField(default='0', max_length=2)),
                ('d60', models.CharField(default='0', max_length=2)),
                ('d61', models.CharField(default='0', max_length=2)),
                ('d62', models.CharField(default='0', max_length=2)),
                ('d63', models.CharField(default='0', max_length=2)),
                ('d64', models.CharField(default='0', max_length=2)),
                ('d65', models.CharField(default='0', max_length=2)),
                ('d66', models.CharField(default='0', max_length=2)),
                ('d67', models.CharField(default='0', max_length=2)),
                ('d68', models.CharField(default='0', max_length=2)),
                ('d69', models.CharField(default='0', max_length=2)),
                ('d70', models.CharField(default='0', max_length=2)),
                ('d71', models.CharField(default='0', max_length=2)),
                ('d72', models.CharField(default='0', max_length=2)),
                ('d73', models.CharField(default='0', max_length=2)),
                ('d74', models.CharField(default='0', max_length=2)),
                ('d75', models.CharField(default='0', max_length=2)),
                ('d76', models.CharField(default='0', max_length=2)),
                ('d77', models.CharField(default='0', max_length=2)),
                ('d78', models.CharField(default='0', max_length=2)),
                ('d79', models.CharField(default='0', max_length=2)),
                ('d80', models.CharField(default='0', max_length=2)),
                ('d81', models.CharField(default='0', max_length=2)),
                ('d82', models.CharField(default='0', max_length=2)),
                ('d83', models.CharField(default='0', max_length=2)),
                ('d84', models.CharField(default='0', max_length=2)),
                ('d85', models.CharField(default='0', max_length=2)),
                ('d86', models.CharField(default='0', max_length=2)),
                ('d87', models.CharField(default='0', max_length=2)),
                ('d88', models.CharField(default='0', max_length=2)),
                ('d89', models.CharField(default='0', max_length=2)),
                ('d90', models.CharField(default='0', max_length=2)),
                ('d91', models.CharField(default='0', max_length=2)),
                ('d92', models.CharField(default='0', max_length=2)),
                ('d93', models.CharField(default='0', max_length=2)),
                ('d94', models.CharField(default='0', max_length=2)),
                ('d95', models.CharField(default='0', max_length=2)),
                ('d96', models.CharField(default='0', max_length=2)),
                ('d97', models.CharField(default='0', max_length=2)),
                ('d98', models.CharField(default='0', max_length=2)),
                ('d99', models.CharField(default='0', max_length=2)),
                ('d100', models.CharField(default='0', max_length=2)),
                ('d101', models.CharField(default='0', max_length=2)),
                ('d102', models.CharField(default='0', max_length=2)),
                ('d103', models.CharField(default='0', max_length=2)),
                ('d104', models.CharField(default='0', max_length=2)),
                ('d105', models.CharField(default='0', max_length=2)),
                ('d106', models.CharField(default='0', max_length=2)),
                ('d107', models.CharField(default='0', max_length=2)),
                ('d108', models.CharField(default='0', max_length=2)),
                ('d109', models.CharField(default='0', max_length=2)),
                ('d110', models.CharField(default='0', max_length=2)),
                ('d111', models.CharField(default='0', max_length=2)),
                ('d112', models.CharField(default='0', max_length=2)),
                ('d113', models.CharField(default='0', max_length=2)),
                ('d114', models.CharField(default='0', max_length=2)),
                ('d115', models.CharField(default='0', max_length=2)),
                ('d116', models.CharField(default='0', max_length=2)),
                ('d117', models.CharField(default='0', max_length=2)),
                ('d118', models.CharField(default='0', max_length=2)),
                ('d119', models.CharField(default='0', max_length=2)),
                ('d120', models.CharField(default='0', max_length=2)),
                ('d121', models.CharField(default='0', max_length=2)),
                ('d122', models.CharField(default='0', max_length=2)),
                ('d123', models.CharField(default='0', max_length=2)),
                ('d124', models.CharField(default='0', max_length=2)),
                ('d125', models.CharField(default='0', max_length=2)),
                ('d126', models.CharField(default='0', max_length=2)),
                ('d127', models.CharField(default='0', max_length=2)),
                ('d128', models.CharField(default='0', max_length=2)),
                ('d129', models.CharField(default='0', max_length=2)),
                ('d130', models.CharField(default='0', max_length=2)),
                ('d131', models.CharField(default='0', max_length=2)),
                ('d132', models.CharField(default='0', max_length=2)),
                ('d133', models.CharField(default='0', max_length=2)),
                ('d134', models.CharField(default='0', max_length=2)),
                ('d135', models.CharField(default='0', max_length=2)),
                ('d136', models.CharField(default='0', max_length=2)),
                ('d137', models.CharField(default='0', max_length=2)),
                ('d138', models.CharField(default='0', max_length=2)),
                ('d139', models.CharField(default='0', max_length=2)),
                ('d140', models.CharField(default='0', max_length=2)),
                ('d141', models.CharField(default='0', max_length=2)),
                ('d142', models.CharField(default='0', max_length=2)),
                ('d143', models.CharField(default='0', max_length=2)),
                ('d144', models.CharField(default='0', max_length=2)),
                ('d145', models.CharField(default='0', max_length=2)),
                ('d146', models.CharField(default='0', max_length=2)),
                ('d147', models.CharField(default='0', max_length=2)),
                ('d148', models.CharField(default='0', max_length=2)),
                ('d149', models.CharField(default='0', max_length=2)),
                ('d150', models.CharField(default='0', max_length=2)),
                ('d151', models.CharField(default='0', max_length=2)),
                ('d152', models.CharField(default='0', max_length=2)),
                ('d153', models.CharField(default='0', max_length=2)),
                ('d154', models.CharField(default='0', max_length=2)),
                ('d155', models.CharField(default='0', max_length=2)),
                ('d156', models.CharField(default='0', max_length=2)),
                ('d157', models.CharField(default='0', max_length=2)),
                ('d158', models.CharField(default='0', max_length=2)),
                ('d159', models.CharField(default='0', max_length=2)),
                ('d160', models.CharField(default='0', max_length=2)),
                ('d161', models.CharField(default='0', max_length=2)),
                ('d162', models.CharField(default='0', max_length=2)),
                ('d163', models.CharField(default='0', max_length=2)),
                ('d164', models.CharField(default='0', max_length=2)),
                ('d165', models.CharField(default='0', max_length=2)),
                ('d166', models.CharField(default='0', max_length=2)),
                ('d167', models.CharField(default='0', max_length=2)),
                ('d168', models.CharField(default='0', max_length=2)),
                ('d169', models.CharField(default='0', max_length=2)),
                ('d170', models.CharField(default='0', max_length=2)),
                ('d171', models.CharField(default='0', max_length=2)),
                ('d172', models.CharField(default='0', max_length=2)),
                ('d173', models.CharField(default='0', max_length=2)),
                ('d174', models.CharField(default='0', max_length=2)),
                ('d175', models.CharField(default='0', max_length=2)),
                ('d176', models.CharField(default='0', max_length=2)),
                ('d177', models.CharField(default='0', max_length=2)),
                ('d178', models.CharField(default='0', max_length=2)),
                ('d179', models.CharField(default='0', max_length=2)),
                ('d180', models.CharField(default='0', max_length=2)),
                ('d181', models.CharField(default='0', max_length=2)),
                ('d182', models.CharField(default='0', max_length=2)),
                ('d183', models.CharField(default='0', max_length=2)),
                ('d184', models.CharField(default='0', max_length=2)),
                ('d185', models.CharField(default='0', max_length=2)),
                ('d186', models.CharField(default='0', max_length=2)),
                ('d187', models.CharField(default='0', max_length=2)),
                ('d188', models.CharField(default='0', max_length=2)),
                ('d189', models.CharField(default='0', max_length=2)),
                ('d190', models.CharField(default='0', max_length=2)),
                ('d191', models.CharField(default='0', max_length=2)),
                ('d192', models.CharField(default='0', max_length=2)),
                ('d193', models.CharField(default='0', max_length=2)),
                ('d194', models.CharField(default='0', max_length=2)),
                ('d195', models.CharField(default='0', max_length=2)),
                ('d196', models.CharField(default='0', max_length=2)),
                ('d197', models.CharField(default='0', max_length=2)),
                ('d198', models.CharField(default='0', max_length=2)),
                ('d199', models.CharField(default='0', max_length=2)),
                ('d200', models.CharField(default='0', max_length=2)),
                ('d201', models.CharField(default='0', max_length=2)),
                ('d202', models.CharField(default='0', max_length=2)),
                ('d203', models.CharField(default='0', max_length=2)),
                ('d204', models.CharField(default='0', max_length=2)),
                ('d205', models.CharField(default='0', max_length=2)),
                ('d206', models.CharField(default='0', max_length=2)),
                ('d207', models.CharField(default='0', max_length=2)),
                ('d208', models.CharField(default='0', max_length=2)),
                ('d209', models.CharField(default='0', max_length=2)),
                ('d210', models.CharField(default='0', max_length=2)),
                ('d211', models.CharField(default='0', max_length=2)),
                ('d212', models.CharField(default='0', max_length=2)),
                ('d213', models.CharField(default='0', max_length=2)),
                ('d214', models.CharField(default='0', max_length=2)),
                ('d215', models.CharField(default='0', max_length=2)),
                ('d216', models.CharField(default='0', max_length=2)),
                ('d217', models.CharField(default='0', max_length=2)),
                ('d218', models.CharField(default='0', max_length=2)),
                ('d219', models.CharField(default='0', max_length=2)),
                ('d220', models.CharField(default='0', max_length=2)),
                ('d221', models.CharField(default='0', max_length=2)),
                ('d222', models.CharField(default='0', max_length=2)),
                ('d223', models.CharField(default='0', max_length=2)),
                ('d224', models.CharField(default='0', max_length=2)),
                ('d225', models.CharField(default='0', max_length=2)),
                ('d226', models.CharField(default='0', max_length=2)),
                ('d227', models.CharField(default='0', max_length=2)),
                ('d228', models.CharField(default='0', max_length=2)),
                ('d229', models.CharField(default='0', max_length=2)),
                ('d230', models.CharField(default='0', max_length=2)),
                ('d231', models.CharField(default='0', max_length=2)),
                ('d232', models.CharField(default='0', max_length=2)),
                ('d233', models.CharField(default='0', max_length=2)),
                ('d234', models.CharField(default='0', max_length=2)),
                ('d235', models.CharField(default='0', max_length=2)),
                ('d236', models.CharField(default='0', max_length=2)),
                ('d237', models.CharField(default='0', max_length=2)),
                ('d238', models.CharField(default='0', max_length=2)),
                ('d239', models.CharField(default='0', max_length=2)),
                ('d240', models.CharField(default='0', max_length=2)),
                ('d241', models.CharField(default='0', max_length=2)),
                ('d242', models.CharField(default='0', max_length=2)),
                ('d243', models.CharField(default='0', max_length=2)),
                ('d244', models.CharField(default='0', max_length=2)),
                ('d245', models.CharField(default='0', max_length=2)),
                ('d246', models.CharField(default='0', max_length=2)),
                ('d247', models.CharField(default='0', max_length=2)),
                ('d248', models.CharField(default='0', max_length=2)),
                ('d249', models.CharField(default='0', max_length=2)),
                ('d250', models.CharField(default='0', max_length=2)),
                ('d251', models.CharField(default='0', max_length=2)),
                ('d252', models.CharField(default='0', max_length=2)),
                ('d253', models.CharField(default='0', max_length=2)),
                ('d254', models.CharField(default='0', max_length=2)),
                ('d255', models.CharField(default='0', max_length=2)),
                ('d256', models.CharField(default='0', max_length=2)),
                ('d257', models.CharField(default='0', max_length=2)),
                ('d258', models.CharField(default='0', max_length=2)),
                ('d259', models.CharField(default='0', max_length=2)),
                ('d260', models.CharField(default='0', max_length=2)),
                ('d261', models.CharField(default='0', max_length=2)),
                ('d262', models.CharField(default='0', max_length=2)),
                ('d263', models.CharField(default='0', max_length=2)),
                ('d264', models.CharField(default='0', max_length=2)),
                ('d265', models.CharField(default='0', max_length=2)),
                ('d266', models.CharField(default='0', max_length=2)),
                ('d267', models.CharField(default='0', max_length=2)),
                ('d268', models.CharField(default='0', max_length=2)),
                ('d269', models.CharField(default='0', max_length=2)),
                ('d270', models.CharField(default='0', max_length=2)),
                ('d271', models.CharField(default='0', max_length=2)),
                ('d272', models.CharField(default='0', max_length=2)),
                ('d273', models.CharField(default='0', max_length=2)),
                ('d274', models.CharField(default='0', max_length=2)),
                ('d275', models.CharField(default='0', max_length=2)),
                ('d276', models.CharField(default='0', max_length=2)),
                ('d277', models.CharField(default='0', max_length=2)),
                ('d278', models.CharField(default='0', max_length=2)),
                ('d279', models.CharField(default='0', max_length=2)),
                ('d280', models.CharField(default='0', max_length=2)),
                ('d281', models.CharField(default='0', max_length=2)),
                ('d282', models.CharField(default='0', max_length=2)),
                ('d283', models.CharField(default='0', max_length=2)),
                ('d284', models.CharField(default='0', max_length=2)),
                ('d285', models.CharField(default='0', max_length=2)),
                ('d286', models.CharField(default='0', max_length=2)),
                ('d287', models.CharField(default='0', max_length=2)),
                ('d288', models.CharField(default='0', max_length=2)),
                ('d289', models.CharField(default='0', max_length=2)),
                ('d290', models.CharField(default='0', max_length=2)),
                ('d291', models.CharField(default='0', max_length=2)),
                ('d292', models.CharField(default='0', max_length=2)),
                ('d293', models.CharField(default='0', max_length=2)),
                ('d294', models.CharField(default='0', max_length=2)),
                ('d295', models.CharField(default='0', max_length=2)),
                ('d296', models.CharField(default='0', max_length=2)),
                ('d297', models.CharField(default='0', max_length=2)),
                ('d298', models.CharField(default='0', max_length=2)),
                ('d299', models.CharField(default='0', max_length=2)),
                ('d300', models.CharField(default='0', max_length=2)),
                ('d301', models.CharField(default='0', max_length=2)),
                ('d302', models.CharField(default='0', max_length=2)),
                ('d303', models.CharField(default='0', max_length=2)),
                ('d304', models.CharField(default='0', max_length=2)),
                ('d305', models.CharField(default='0', max_length=2)),
                ('d306', models.CharField(default='0', max_length=2)),
                ('d307', models.CharField(default='0', max_length=2)),
                ('d308', models.CharField(default='0', max_length=2)),
                ('d309', models.CharField(default='0', max_length=2)),
                ('d310', models.CharField(default='0', max_length=2)),
                ('d311', models.CharField(default='0', max_length=2)),
                ('d312', models.CharField(default='0', max_length=2)),
                ('d313', models.CharField(default='0', max_length=2)),
                ('d314', models.CharField(default='0', max_length=2)),
                ('d315', models.CharField(default='0', max_length=2)),
                ('d316', models.CharField(default='0', max_length=2)),
                ('d317', models.CharField(default='0', max_length=2)),
                ('d318', models.CharField(default='0', max_length=2)),
                ('d319', models.CharField(default='0', max_length=2)),
                ('d320', models.CharField(default='0', max_length=2)),
                ('d321', models.CharField(default='0', max_length=2)),
                ('d322', models.CharField(default='0', max_length=2)),
                ('d323', models.CharField(default='0', max_length=2)),
                ('d324', models.CharField(default='0', max_length=2)),
                ('d325', models.CharField(default='0', max_length=2)),
                ('d326', models.CharField(default='0', max_length=2)),
                ('d327', models.CharField(default='0', max_length=2)),
                ('d328', models.CharField(default='0', max_length=2)),
                ('d329', models.CharField(default='0', max_length=2)),
                ('d330', models.CharField(default='0', max_length=2)),
                ('d331', models.CharField(default='0', max_length=2)),
                ('d332', models.CharField(default='0', max_length=2)),
                ('d333', models.CharField(default='0', max_length=2)),
                ('d334', models.CharField(default='0', max_length=2)),
                ('d335', models.CharField(default='0', max_length=2)),
                ('d336', models.CharField(default='0', max_length=2)),
                ('d337', models.CharField(default='0', max_length=2)),
                ('d338', models.CharField(default='0', max_length=2)),
                ('d339', models.CharField(default='0', max_length=2)),
                ('d340', models.CharField(default='0', max_length=2)),
                ('d341', models.CharField(default='0', max_length=2)),
                ('d342', models.CharField(default='0', max_length=2)),
                ('d343', models.CharField(default='0', max_length=2)),
                ('d344', models.CharField(default='0', max_length=2)),
                ('d345', models.CharField(default='0', max_length=2)),
                ('d346', models.CharField(default='0', max_length=2)),
                ('d347', models.CharField(default='0', max_length=2)),
                ('d348', models.CharField(default='0', max_length=2)),
                ('d349', models.CharField(default='0', max_length=2)),
                ('d350', models.CharField(default='0', max_length=2)),
                ('d351', models.CharField(default='0', max_length=2)),
                ('d352', models.CharField(default='0', max_length=2)),
                ('d353', models.CharField(default='0', max_length=2)),
                ('d354', models.CharField(default='0', max_length=2)),
                ('d355', models.CharField(default='0', max_length=2)),
                ('d356', models.CharField(default='0', max_length=2)),
                ('d357', models.CharField(default='0', max_length=2)),
                ('d358', models.CharField(default='0', max_length=2)),
                ('d359', models.CharField(default='0', max_length=2)),
                ('d360', models.CharField(default='0', max_length=2)),
                ('d361', models.CharField(default='0', max_length=2)),
                ('d362', models.CharField(default='0', max_length=2)),
                ('d363', models.CharField(default='0', max_length=2)),
                ('d364', models.CharField(default='0', max_length=2)),
                ('d365', models.CharField(default='0', max_length=2)),
                ('d366', models.CharField(default='0', max_length=2)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roomManager.room')),
            ],
        ),
    ]