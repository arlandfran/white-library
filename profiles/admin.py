from django.contrib import admin

from .models import UserProfile, Address


class AddressAdminInline(admin.TabularInline):
    model = Address
    exclude = ['user']

    show_change_link = True
    extra = 0


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):

    def addresses(self, obj):
        return obj.addresses.count()

    inlines = (AddressAdminInline,)

    fields = ('user',)

    list_display = ('user', 'addresses',)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):

    fields = ('profile', 'default', 'phone_number', 'street_address1',
              'street_address2', 'town_or_city', 'county', 'postcode', 'country',)

    list_display = ('profile', 'default', 'phone_number', 'street_address1',
                    'street_address2', 'town_or_city', 'county', 'postcode', 'country',)
