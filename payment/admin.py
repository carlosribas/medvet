from forms import PaymentForm, ServiceItemForm
from django.contrib import admin
from payment.models import *


admin.site.register(ServiceType)


class ServiceItemInline(admin.TabularInline):
    model = ServiceItem
    extra = 1
    form = ServiceItemForm


class PaymentAdmin(admin.ModelAdmin):
    fields = ['owner', 'date']
    list_display = ('date', 'owner', 'animal', 'total', 'balance', 'status')
    list_display_links = ('date',)
    search_fields = ['owner__name']
    inlines = (ServiceItemInline,)
    form = PaymentForm

admin.site.register(Payment, PaymentAdmin)