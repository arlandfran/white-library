from django.contrib import admin

from .models import UserProfile


class ProfileAdmin(admin.ModelAdmin):

    fields = ('user', 'phone_number', 'street_address1',
              'street_address2', 'town_or_city', 'county', 'postcode', 'country')

    list_display = ('user',)


admin.site.register(UserProfile, ProfileAdmin)
