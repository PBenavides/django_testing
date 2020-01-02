from django import forms
from .models import Sensores

class SensoresForm(forms.ModelForm):
    class Meta:
        model = Sensores
        fields = [
            'nombre',
            'id_mcu',
            'nro_piscina',
            'nro_sensores',
        ]