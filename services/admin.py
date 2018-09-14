from django.contrib import admin
from services.models import ConsultationType, ExamCategory, ExamName, VaccineType


admin.site.register(ConsultationType)
admin.site.register(ExamCategory)
admin.site.register(ExamName)
admin.site.register(VaccineType)
