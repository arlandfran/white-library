from django.contrib import admin

from .models import Address


class AddressAdmin(admin.ModelAdmin):

    fields = ('profile', 'default', 'phone_number', 'street_address1',
              'street_address2', 'town_or_city', 'county', 'postcode', 'country',)

    list_display = ('profile', 'default', 'phone_number', 'street_address1',
                    'street_address2', 'town_or_city', 'county', 'postcode', 'country',)


admin.site.register(Address, AddressAdmin)
