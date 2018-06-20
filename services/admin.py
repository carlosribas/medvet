from django.contrib import admin
from models import ConsultationType, ExamCategory, ExamType, VaccineType


admin.site.register(ConsultationType)
admin.site.register(ExamCategory)
admin.site.register(ExamType)
admin.site.register(VaccineType)
