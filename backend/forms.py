from .models import *
from django import forms
from .widgets import *


class ActiveForm(forms.ModelForm):

    info = forms.Field(label="Información adicional", required=False,
                       widget=JsonWidget)

    class Meta:
        model = Active
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        if instance:
            kwargs.update(initial={
                'info': instance
            })
        super().__init__(*args, **kwargs)


