# Generated by Django 4.0.2 on 2022-07-18 07:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='P2PTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_payable', models.DecimalField(decimal_places=4, help_text='The amount debted to the producer by the consumer in this trade.', max_digits=10, verbose_name='amount_payable_by_consumer')),
                ('closing', models.DateTimeField(help_text='The date time at which the transaction closed.', verbose_name='closing_datetime')),
                ('exported_energy', models.IntegerField(help_text='The energy exported by the producer in kWh', verbose_name='exported_energy')),
                ('meta', models.JSONField(help_text='Metadata for the transaction', verbose_name='metadata')),
                ('opening', models.DateTimeField(default=django.utils.timezone.now, help_text='The date time at which the transaction opened.', verbose_name='opening_datetime')),
                ('transmission_distance', models.IntegerField(blank=True, help_text='The transmission distance in metres.', null=True, verbose_name='transmission_distance')),
                ('transmission_efficiency', models.DecimalField(decimal_places=4, help_text='How efficiently the energy trade made between the prosumers.', max_digits=4, verbose_name='transmission_efficiency')),
                ('unit_price', models.DecimalField(decimal_places=4, help_text='The weighted average unit price for the exported energy', max_digits=10, verbose_name='weighted_avg_unit_price')),
                ('upi_payment_url', models.CharField(help_text='The URL for initiating UPI payment.', max_length=255, verbose_name='upi_payment_url')),
            ],
        ),
    ]
