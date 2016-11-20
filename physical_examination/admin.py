from forms import *
from django.contrib import admin
from physical_examination.models import *
from django.utils.translation import ugettext_lazy as _


class ExaminationAdmin(admin.ModelAdmin):

    fieldsets = (
        (_('Examination info'), {
            'fields': ('date', 'owner', 'animal', 'temperature', 'bodyweight', 'body_condition',)
        }),
        (_('Cardiorespiratory System'), {
            'fields': ('pulmonary_auscultation', 'pulmonary_auscultation_note', 'respiratory_rate',
                       'cardiac_auscultation', 'cardiac_auscultation_note', 'heart_rate', 'pulse', 'pulse_note')
        }),
        (_('Other info'), {
            'fields': ('attitude', 'attitude_note', 'face', 'face_note', 'eye', 'eye_note', 'ear', 'ear_note', 
                       'nose', 'nose_note', 'hydration', 'mouth', 'mouth_note', 'mucous_membrane', 
                       'capillary_refill_time', 'superficial_lymph_nodes', 'superficial_lymph_nodes_note', 
                       'palpable_thyroid', 'palpable_thyroid_note', 'abdominal_palpation', 'abdominal_palpation_note',
                       'coat', 'coat_note', 'skin', 'skin_note', 'musculoskeletal_system',
                       'musculoskeletal_system_note', 'central_and_peripheral_nervous_system',
                       'central_and_peripheral_nervous_system_note',)
        }),
        (_('Additional Findings'), {
            'fields': ('additional_findings',)
        }),
    )

    list_display = ('date', 'animal', 'owner')
    list_display_links = ('date',)
    search_fields = ['animal__animal_name', 'animal__owner__name']

admin.site.register(Examination, ExaminationAdmin)
