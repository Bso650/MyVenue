# Generated by Django 3.1.6 on 2021-03-03 05:17

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_delete_orderdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='name',
            new_name='venue_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='date',
        ),
        migrations.AddField(
            model_name='order',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='date_booked_for',
            field=models.DateField(default=datetime.datetime(2021, 3, 3, 5, 16, 6, 947367, tzinfo=utc), verbose_name='Date Booked for'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Ordered Date and Time'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='user_address',
            field=models.CharField(default='Buwtwa', max_length=200, verbose_name='Address of User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='user_email',
            field=models.EmailField(default='bimal@bimal.com', max_length=254, verbose_name='User Email'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='user_phone_number',
            field=models.BigIntegerField(default=986677, verbose_name='Contact Number of User'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(max_length=12, verbose_name='Order ID'),
        ),
    ]
