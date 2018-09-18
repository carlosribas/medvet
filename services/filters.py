import django_filters

from django_filters.widgets import RangeWidget
from services.models import Service, Vaccine


class ServiceFilter(django_filters.FilterSet):
    date = django_filters.DateFromToRangeFilter(widget=RangeWidget(attrs={'class': 'form-control datepicker'}))

    def __init__(self, *args, **kwargs):
        super(ServiceFilter, self).__init__(*args, **kwargs)
        self.form.fields['date'].fields[0].input_formats = ['%d/%m/%Y']
        self.form.fields['date'].fields[-1].input_formats = ['%d/%m/%Y']

    class Meta:
        model = Service
        fields = ['date']


class VaccineBoosterFilter(django_filters.FilterSet):
    booster = django_filters.DateFromToRangeFilter(widget=RangeWidget(attrs={'class': 'form-control datepicker'}))

    def __init__(self, *args, **kwargs):
        super(VaccineBoosterFilter, self).__init__(*args, **kwargs)
        self.form.fields['booster'].fields[0].input_formats = ['%d/%m/%Y']
        self.form.fields['booster'].fields[-1].input_formats = ['%d/%m/%Y']

    class Meta:
        model = Vaccine
        fields = ['booster']
