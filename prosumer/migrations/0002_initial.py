# Generated by Django 4.0.2 on 2022-05-29 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('prosumer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prosumer',
            name='user',
            field=models.ForeignKey(help_text='The user associated to the prosumer', on_delete=django.db.models.deletion.PROTECT, related_name='prosumers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='load',
            name='prosumer',
            field=models.ForeignKey(help_text='The prosumer associated to the load subsystem.', on_delete=django.db.models.deletion.PROTECT, related_name='loads', to='prosumer.prosumer', verbose_name='prosumer'),
        ),
        migrations.AddField(
            model_name='generation',
            name='prosumer',
            field=models.ForeignKey(help_text='The prosumer of this generation subsystem.', on_delete=django.db.models.deletion.PROTECT, related_name='generations', to='prosumer.prosumer', verbose_name='prosumer'),
        ),
    ]
