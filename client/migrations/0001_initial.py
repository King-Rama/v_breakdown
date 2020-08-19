# Generated by Django 3.0 on 2020-08-19 12:39

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
            name='HelpProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=500, null=True)),
                ('technician', models.CharField(blank=True, max_length=100, null=True)),
                ('facility_name', models.CharField(max_length=100)),
                ('zone', models.PositiveSmallIntegerField(choices=[(1, 'ilala'), (2, 'temeke'), (3, 'kinondoni'), (4, 'ubungo')], default=1)),
                ('available_status', models.BooleanField(default=False)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/garage/<django.db.models.fields.CharField>/%Y')),
                ('description', models.TextField(blank=True)),
                ('manager', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='garage', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BreakDownRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_location', models.CharField(blank=True, max_length=500, null=True)),
                ('fix_location', models.CharField(blank=True, max_length=500, null=True)),
                ('breakdown_description', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('end_trip', models.DateTimeField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Waiting'), (2, 'Picked'), (3, 'Ready'), (4, 'Cancel'), (5, 'Ended')], default=1)),
                ('towing', models.BooleanField(default=False)),
                ('flat_tire', models.BooleanField(default=False)),
                ('engine_down', models.BooleanField(default=False)),
                ('client_zone', models.PositiveSmallIntegerField(choices=[(1, 'ilala'), (2, 'temeke'), (3, 'kinondoni'), (4, 'ubungo')], default=1, verbose_name='zone')),
                ('testimonials', models.TextField(blank=True, null=True)),
                ('vehicle', models.PositiveSmallIntegerField(choices=[(1, 'moto'), (2, 'mini car'), (3, 'coupe'), (4, 'mini van'), (5, 'pickup'), (6, 'limo'), (7, 'sedan'), (8, 'truck'), (9, 'no idea')], default=2)),
                ('garage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='garages', to='client.HelpProvider')),
                ('requesting_client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='client', to=settings.AUTH_USER_MODEL)),
                ('technician', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='techs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
