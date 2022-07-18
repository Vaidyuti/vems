# Generated by Django 4.0.2 on 2022-07-18 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('prosumer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='p2ptransaction',
            name='consumer',
            field=models.ForeignKey(help_text='The prosumer which imported the energy after transmission and other losses.', on_delete=django.db.models.deletion.PROTECT, related_name='p2_p_transactions_consumer', to='prosumer.prosumer', verbose_name='energy_consumer'),
        ),
        migrations.AddField(
            model_name='p2ptransaction',
            name='producer',
            field=models.ForeignKey(help_text='The prosumer which exported the energy.', on_delete=django.db.models.deletion.PROTECT, related_name='p2_p_transactions_producer', to='prosumer.prosumer', verbose_name='energy_producer'),
        ),
    ]