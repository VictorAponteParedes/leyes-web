from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML
from .models import Caso, Cliente, Abogado

class CasoForm(forms.ModelForm):
    class Meta:
        model = Caso
        fields = ['nombre', 'nro_expediente', 'fecha','materia','juzgado', "foto_perfil"]
        labels = {
            'nombre': 'Nombre del Caso',
            'nro_expediente': 'Número de Expediente',
            'fecha': 'Fecha del Caso',
            'materia': 'Materia Legal',
            'juzgado': 'Juzgado Asignado',
            'foto_perfil': 'Foto del Caso'
        }
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['nombre'].widget.attrs['class'] = 'transparent-input'
        self.fields['nro_expediente'].widget.attrs['class'] = 'transparent-input'
        self.fields['fecha'].widget.attrs['class'] = 'transparent-input'
        self.fields['materia'].widget.attrs['class'] = 'transparent-input'
        self.fields['juzgado'].widget.attrs['class'] = 'transparent-input'
        self.fields['foto_perfil'].widget.attrs['class'] = 'transparent-input'
        self.helper.form_method = 'post'
        self.helper.form_enctype = 'multipart/form-data'
        
        


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'edad', 'telefono','caso_relacionado', "is_activo" , "foto_perfil"]
        labels = {
            "is_activo":"Cliente activo"

        }
       

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['nombre'].widget.attrs['class'] = 'transparent-input'
        self.fields['edad'].widget.attrs['class'] = 'transparent-input'
        self.fields['telefono'].widget.attrs['class'] = 'transparent-input'
        self.fields['caso_relacionado'].widget.attrs['class'] = 'transparent-input'
        self.fields['is_activo'].widget.attrs['class'] = 'transparent-input'
        self.fields['foto_perfil'].widget.attrs['class'] = 'transparent-input'

        self.helper.form_method = 'post'
        self.helper.form_enctype = 'multipart/form-data'
       


class AbogadoForm(forms.ModelForm):
    class Meta:
        model = Abogado
        fields = ['nombre', 'edad', 'telefono','cliente_relacionado',"foto_perfil" , "especialidad" , "descripcion"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['nombre'].widget.attrs['class'] = 'transparent-input'
        self.fields['edad'].widget.attrs['class'] = 'transparent-input'
        self.fields['telefono'].widget.attrs['class'] = 'transparent-input'
        self.fields['cliente_relacionado'].widget.attrs['class'] = 'transparent-input'
        self.fields['foto_perfil'].widget.attrs['class'] = 'transparent-input'
        self.fields['especialidad'].widget.attrs['class'] = 'transparent-input'
        self.fields['descripcion'].widget.attrs['class'] = 'transparent-input'
        self.helper.form_method = 'post'
        self.helper.form_enctype = 'multipart/form-data'






