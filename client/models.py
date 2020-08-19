from django.conf import settings
from django.db import models
from django.urls import reverse


class HelpProvider(models.Model):
    ZONES_CHOICES = (
        # to simplify finding nearest help provider
        (1, 'ilala'),
        (2, 'temeke'),
        (3, 'kinondoni'),
        (4, 'ubungo')
    )

    manager = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='garage', on_delete=models.CASCADE)
    location = models.CharField(max_length=500, blank=True, null=True)
    technician = models.CharField(max_length=100, blank=True, null=True)
    facility_name = models.CharField(max_length=100)
    zone = models.PositiveSmallIntegerField(choices=ZONES_CHOICES, default=1)
    available_status = models.BooleanField(default=False)
    photo = models.ImageField(upload_to=f'images/garage/{facility_name}/%Y', blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.manager.username


class BreakDownRequest(models.Model):
    """
    this model will be the model for the whole process.
    """
    ZONES_CHOICES = (
        # to simplify finding nearest help provider
        (1, 'ilala'),
        (2, 'temeke'),
        (3, 'kinondoni'),
        (4, 'ubungo')
    )

    TRIP_CHOICES = (
        (1, 'Waiting'),
        (2, 'Picked'),
        (3, 'Ready'),
        (4, 'Cancel'),
        (5, 'Ended'),
    )

    CAR_TYPE = (
        (1, 'moto'),
        (2, 'mini car'),
        (3, 'coupe'),
        (4, 'mini van'),
        (5, 'pickup'),
        (6, 'limo'),
        (7, 'sedan'),
        (8, 'truck'),
        (9, 'no idea')
    )

    requesting_client = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='client',
                                          on_delete=models.DO_NOTHING, null=True)
    garage = models.ForeignKey(HelpProvider, on_delete=models.DO_NOTHING, null=True, related_name='garages', blank=True)
    client_location = models.CharField(max_length=500, blank=True, null=True)
    fix_location = models.CharField(max_length=500, blank=True, null=True)
    breakdown_description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    end_trip = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(default=True)
    status = models.PositiveSmallIntegerField(choices=TRIP_CHOICES, default=1)
    towing = models.BooleanField(default=False)
    flat_tire = models.BooleanField(default=False)
    engine_down = models.BooleanField(default=False)
    client_zone = models.PositiveSmallIntegerField('zone', choices=ZONES_CHOICES, default=1)
    testimonials = models.TextField(blank=True, null=True)
    technician = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='techs',
                                          on_delete=models.DO_NOTHING, null=True)
    vehicle = models.PositiveSmallIntegerField(choices=CAR_TYPE, default=2)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('client:emergency-detail', args=[self.id])
