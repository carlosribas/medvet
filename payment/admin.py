from forms import PaymentForm, ServiceItemForm
from django.contrib import admin
from payment.models import *


admin.site.register(ServiceType)


class ServiceItemInline(admin.TabularInline):
    model = ServiceItem
    extra = 1
    form = ServiceItemForm


class PaymentAdmin(admin.ModelAdmin):
    fields = ['owner', 'date', 'status', 'total', 'balance']
    list_display = ('owner', 'date', 'status', 'total', 'balance')
    list_display_links = ('total',)
    search_fields = ['owner__name']
    inlines = (ServiceItemInline,)
    form = PaymentForm

admin.site.register(Payment, PaymentAdmin)