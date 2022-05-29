# Generated by Django 4.0.2 on 2022-05-29 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Generation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_value', models.IntegerField(blank=True, help_text='The value of the generation subsystem asset in local currency', null=True, verbose_name='asset_value')),
                ('conversion_technique', models.CharField(choices=[('FBR', 'Fast Breeder'), ('GCC', 'GCC'), ('LWR', 'LWR'), ('IGCC', 'IGCC'), ('SOFC', 'SOFC'), ('WIND', 'Wind Power'), ('HYDRO', 'Hydro Power'), ('OTHER', 'Other'), ('SOLAR', 'Photo Voltaic'), ('LWR_Pu', 'Pu-thermal'), ('GEOTHERMAL', 'Geothermal'), ('CONVENTIONAL', 'Conventional')], help_text='The conversion technique of the generation subsystem', max_length=255, verbose_name='conversion_technique')),
                ('efficiency', models.DecimalField(decimal_places=4, help_text='Efficiency of the subsystem (in %)', max_digits=4, verbose_name='subsystem_efficiency')),
                ('installed_capacity', models.IntegerField(help_text='Installed Capacity in KW', verbose_name='installed_capacity_kw')),
                ('payback_period', models.IntegerField(blank=True, help_text='Payback period of the generation subsystem asset in months', null=True, verbose_name='payback_period')),
                ('primary_energy', models.CharField(choices=[('OIL', 'Oil'), ('COAL', 'Coal'), ('OTHER', 'Other'), ('BIOMASS', 'Biomass'), ('NUCLEAR', 'Nuclear'), ('RENEWABLES', 'Renewables'), ('NATURAL_GAS', 'Natural Gas')], help_text='The primary energy type of the generation subsystem.', max_length=255, verbose_name='primary_energy_type')),
            ],
        ),
        migrations.CreateModel(
            name='Load',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_dr_adaptive', models.BooleanField(default=False, help_text='Whether the load subsystem is adaptive to demand response signals.', verbose_name='is_demand_response_adaptive')),
                ('max_power', models.IntegerField(help_text='The maximum power in kW that the load may demand at any instant.', verbose_name='max_power_kw')),
            ],
        ),
        migrations.CreateModel(
            name='Prosumer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geolocation', models.JSONField(help_text='Geographic location coordinates of the prosumer', verbose_name='location_coordinates')),
                ('is_dr_adaptive', models.BooleanField(default=False, help_text='Whether the prosumer is adaptive to Demand Response signals.', verbose_name='is_demand_response_adaptive')),
                ('max_export_power', models.IntegerField(help_text='Maximum Export Power in KW', verbose_name='max_export_power')),
                ('max_import_power', models.IntegerField(help_text='Maximum Import Power in KW', verbose_name='max_import_power_kw')),
                ('mean_payback_period', models.IntegerField(blank=True, help_text='Weighted average payback period in terms of months dervied from payback period and asset value of subsystems of the prosumer.', null=True, verbose_name='mean_payback_period')),
                ('total_asset_value', models.IntegerField(blank=True, help_text='The total asset value of the prosumer which shall be used to decide the energy export price.', null=True, verbose_name='total_asset_value')),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('health', models.DecimalField(blank=True, decimal_places=3, help_text='The health of the energy storage system (primarily for battery based storages)', max_digits=3, null=True, verbose_name='storage_health_percentage')),
                ('installed_capacity', models.IntegerField(help_text='The amount of energy storable by the system in kWh.', verbose_name='installed_capacity_kwh')),
                ('technology', models.CharField(choices=[('OTHER', 'Other'), ('LEAD_ACID', 'Lead Acid'), ('LITHIUM_ION', 'Li-Ion')], help_text='The type of technology used for energy storage', max_length=255, verbose_name='storage_technology')),
                ('usable_capacity', models.DecimalField(decimal_places=3, help_text='The depth of discharge allowed for export.', max_digits=3, verbose_name='usable_capacity')),
                ('prosumer', models.ForeignKey(help_text='The prosumer associated with this', on_delete=django.db.models.deletion.PROTECT, related_name='storages', to='prosumer.prosumer', verbose_name='prosumer')),
            ],
        ),
    ]
