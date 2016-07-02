from django.contrib import admin
from forms import ClientAdminForm
from models import Client, ClientContact
from django.utils.translation import ugettext_lazy as _


class ClientContactInline(admin.TabularInline):
    model = ClientContact
    extra = 1


class ClientAdmin(admin.ModelAdmin):

    fieldsets = [
        (None, {
            'fields': ['name', 'email', 'phone', 'cellphone', 'note']
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
    inlines = (ClientContactInline,)
    form = ClientAdminForm

admin.site.register(Client, ClientAdmin)
