import django_filters

from django_filters.widgets import RangeWidget
from services.models import Service


class ServiceFilter(django_filters.FilterSet):
    date = django_filters.DateFromToRangeFilter(widget=RangeWidget(attrs={'class': 'form-control datepicker'}))

    def __init__(self, *args, **kwargs):
        super(ServiceFilter, self).__init__(*args, **kwargs)
        self.form.fields['date'].fields[0].input_formats = ['%d/%m/%Y']
        self.form.fields['date'].fields[-1].input_formats = ['%d/%m/%Y']

    class Meta:
        model = Service
        fields = ['date']
