# Generated by Django 4.2.6 on 2024-02-17 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='area_info',
            fields=[
                ('area_id', models.AutoField(primary_key=True, serialize=False)),
                ('area_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='city_info',
            fields=[
                ('city_id', models.AutoField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='inquiry',
            fields=[
                ('i_id', models.AutoField(primary_key=True, serialize=False)),
                ('i_user_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=40)),
                ('contact', models.IntegerField(max_length=10)),
                ('des', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='pg_owner',
            fields=[
                ('pg_id', models.AutoField(primary_key=True, serialize=False)),
                ('pg_name', models.CharField(max_length=20)),
                ('pg_price', models.IntegerField(max_length=11)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=8)),
                ('location', models.CharField(max_length=50)),
                ('area_rating', models.IntegerField(max_length=10)),
                ('avg_rating', models.IntegerField(max_length=5)),
                ('cover_image', models.CharField(max_length=30)),
                ('des', models.CharField(max_length=30)),
                ('area_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pgfinder_admin.area_info')),
            ],
        ),
        migrations.CreateModel(
            name='pg_room',
            fields=[
                ('pg_room_id', models.AutoField(primary_key=True, serialize=False)),
                ('no_of_room', models.CharField(max_length=50)),
                ('changes', models.CharField(max_length=30)),
                ('pg_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pgfinder_admin.pg_owner')),
            ],
        ),
        migrations.CreateModel(
            name='room_type',
            fields=[
                ('r_id', models.AutoField(primary_key=True, serialize=False)),
                ('r_name', models.CharField(max_length=20)),
                ('des', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='user_info',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=8)),
                ('contact', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('otp', models.IntegerField(max_length=30)),
                ('otp_used', models.CharField(max_length=30)),
                ('is_admin', models.IntegerField(max_length=10)),
                ('area_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pgfinder_admin.area_info')),
            ],
        ),
        migrations.CreateModel(
            name='pg_room_gallary',
            fields=[
                ('gallary_id', models.AutoField(primary_key=True, serialize=False)),
                ('image_patten', models.CharField(max_length=200)),
                ('pg_room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pgfinder_admin.pg_room')),
            ],
        ),
        migrations.AddField(
            model_name='pg_room',
            name='r_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pgfinder_admin.room_type'),
        ),
        migrations.CreateModel(
            name='notifiaction',
            fields=[
                ('n_id', models.AutoField(primary_key=True, serialize=False)),
                ('des', models.CharField(max_length=40)),
                ('n_date', models.DateField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pgfinder_admin.user_info')),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('f_id', models.AutoField(primary_key=True, serialize=False)),
                ('f_date', models.DateField()),
                ('des', models.CharField(max_length=40)),
                ('rating', models.IntegerField(max_length=11)),
                ('pg_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pgfinder_admin.pg_owner')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pgfinder_admin.user_info')),
            ],
        ),
        migrations.CreateModel(
            name='booking',
            fields=[
                ('b_id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.IntegerField(max_length=5)),
                ('b_date', models.DateField()),
                ('payment_status', models.IntegerField(max_length=5)),
                ('payment_amount', models.IntegerField(max_length=50)),
                ('pg_room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pgfinder_admin.pg_room')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pgfinder_admin.user_info')),
            ],
        ),
        migrations.AddField(
            model_name='area_info',
            name='cid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pgfinder_admin.city_info'),
        ),
    ]