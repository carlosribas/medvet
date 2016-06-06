from models import *
from forms import ExamAdminForm
from django.contrib import admin


admin.site.register(Parasitological)
admin.site.register(Hematology)
admin.site.register(RenalProfile)
admin.site.register(HepaticProfile)
admin.site.register(Proteins)
admin.site.register(Endocrinology)
admin.site.register(Electrolytes)
admin.site.register(Microbiology)
admin.site.register(Anatomopathology)
admin.site.register(Image)


class ExamAdmin(admin.ModelAdmin):

    fieldsets = [
        (None, {
            'fields': ('animal', 'date'),
        }),
        ('Parasitological', {
            'classes': ('suit-tab', 'suit-tab-parasitological_exam',),
            'fields': ['parasitological_exam',]}),
        ('Hematology', {
            'classes': ('suit-tab', 'suit-tab-hematology_exam',),
            'fields': ['hematology_exam']}),
        ('Renal profile', {
            'classes': ('suit-tab', 'suit-tab-renal_profile_exam',),
            'fields': ['renal_profile_exam']}),
        ('Hepatic profile', {
            'classes': ('suit-tab', 'suit-tab-hepatic_profile_exam',),
            'fields': ['hepatic_profile_exam']}),
        ('Proteins', {
            'classes': ('suit-tab', 'suit-tab-proteins_exam',),
            'fields': ['proteins_exam']}),
        ('Endocrinology', {
            'classes': ('suit-tab', 'suit-tab-endocrinology_exam',),
            'fields': ['endocrinology_exam']}),
        ('Electrolytes', {
            'classes': ('suit-tab', 'suit-tab-electrolytes_exam',),
            'fields': ['electrolytes_exam']}),
        ('Microbiology', {
            'classes': ('suit-tab', 'suit-tab-microbiology_exam',),
            'fields': ['microbiology_exam']}),
        ('Anatomopathology', {
            'classes': ('suit-tab', 'suit-tab-anatomopathology_exam',),
            'fields': ['anatomopathology_exam']}),
        ('Image', {
            'classes': ('suit-tab', 'suit-tab-image_exam',),
            'fields': ['image_exam']}),
    ]

    suit_form_tabs = (('parasitological_exam', 'Parasitological'), ('hematology_exam', 'Hematology'),
                      ('renal_profile_exam', 'Renal profile'), ('hepatic_profile_exam', 'Hepatic profile'),
                      ('proteins_exam', 'Proteins'), ('endocrinology_exam', 'Endocrinology'),
                      ('electrolytes_exam', 'Electrolytes'), ('microbiology_exam', 'Microbiology'),
                      ('anatomopathology_exam', 'Anatomopathology'), ('image_exam', 'Image'))

    form = ExamAdminForm

admin.site.register(Exam, ExamAdmin)