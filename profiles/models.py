from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """User Profile model for addresses and order history"""
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        # pylint: disable=no-member
        return self.user.username


@receiver(post_save, sender=get_user_model())
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """Create or update user profile"""
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()


class Address(models.Model):

    class Meta:
        verbose_name_plural = 'Addresses'

    default = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(
        blank_label="Country", null=False, blank=False)
    profile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="addresses")

    def save(self, *args, **kwargs):
        """
        Override save method so that if address.default = True,
        set all other addresses related to profile to False
        """
        if self.default:
            self.profile.addresses.all().exclude(
                id=self.id).update(default=False)
        super().save(*args, **kwargs)
