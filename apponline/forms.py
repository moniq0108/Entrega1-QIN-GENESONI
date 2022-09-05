from django import forms


class CarterasFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    codigo = forms.IntegerField()