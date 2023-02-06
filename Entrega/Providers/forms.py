from django import forms

class ProviderForm(forms.Form):
    name = forms.CharField(max_length=100, label= 'Nombre')
    address = forms.CharField(max_length=300, label= 'Dirección')
    phone_number = forms.CharField(max_length=20, label= 'Teléfono')
    email = forms.EmailField(label= 'Correo')
    condition = forms.CharField(max_length=50, label= 'Monot/Resp.Insc')