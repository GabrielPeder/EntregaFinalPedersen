from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, label= 'Nombre')
    model = forms.IntegerField( label= 'Modelo(Año)')
    style = forms.CharField(max_length=50, label= 'Estilo')
    price = forms.IntegerField(label= 'Precio')
    stock = forms.BooleanField(required=False)
    image = forms.ImageField(label= 'Imagen')