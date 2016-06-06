from models import Exam
from django import forms
from django.forms import CheckboxSelectMultiple
# from django.utils.translation import ugettext_lazy as _


class ExamAdminForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super(ExamAdminForm, self).__init__(*args, **kwargs)
    #     self.fields['parasitological_exam'].choices = self.fields['parasitological_exam'].choices[1:]


    class Meta:
        model = Exam

        fields = ['parasitological_exam']

        widgets = {
            'parasitological_exam': CheckboxSelectMultiple(),
        }

    class Media:
        # js = ('/static/js/exam.js',)
        css = {
            'all': ('/static/css/exam_customization.css',)
        }
