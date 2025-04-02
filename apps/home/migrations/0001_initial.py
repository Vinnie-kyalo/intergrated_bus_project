# Generated by Django 3.2.16 on 2025-04-02 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seats_booked', models.IntegerField()),
                ('booking_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed')], default='Pending', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_location', models.CharField(max_length=100)),
                ('to_location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.CharField(choices=[('Mpesa', 'Mpesa'), ('Card', 'Card')], max_length=50)),
                ('payment_status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending', max_length=20)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.booking')),
            ],
        ),
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('departure_time', models.TimeField()),
                ('total_seats', models.IntegerField()),
                ('price_per_seat', models.DecimalField(decimal_places=2, max_digits=10)),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.route')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='bus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.bus'),
        ),
        migrations.AddField(
            model_name='booking',
            name='passenger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.passenger'),
        ),
    ]
