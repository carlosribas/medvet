from django import forms


class ServiceItemForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ServiceItemForm, self).__init__(*args, **kwargs)
        self.fields['value'].widget.attrs['style'] = "width:100px"
