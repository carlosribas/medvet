from django.contrib import admin
from forms import ClientAdminForm
from models import Client
from django.utils.translation import ugettext_lazy as _


class ClientAdmin(admin.ModelAdmin):

    fieldsets = [
        (None, {
            'fields': ['name', 'email', 'phone', 'cellphone', 'note', 'another_responsible',
                       'another_responsible_phone']
        }),
        (_('Address'), {
            'fields': ['zipcode', 'street', 'number', 'street_complement', 'district', 'city', 'state'],
            'classes': ['collapse']
        }),
        (_('Personal info'), {
            'fields': ['rg', 'cpf'],
            'classes': ['collapse']
        }),
    ]

    list_display = ('name', 'email', 'phone', 'cellphone')
    list_display_links = ('name', )
    search_fields = ['name', 'email', 'note', 'cpf']
    form = ClientAdminForm

admin.site.register(Client, ClientAdmin)
