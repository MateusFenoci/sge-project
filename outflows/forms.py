# outflows/forms.py
from django import forms
from django.core.exceptions import ValidationError
from . import models

class OutflowForm(forms.ModelForm):
    class Meta:
        model = models.Outflow
        fields = ['item', 'quantity', 'description']
        widgets = {
            'item': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'item': 'Estoque',
            'quantity': 'Quantidade',
            'description': 'Descrição',
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        item = self.cleaned_data.get('item')

        if item and quantity > item.quantity:
            raise ValidationError(
                f'A quantidade disponível em estoque para o produto {item.product.title} no tamanho {item.size} é de {item.quantity} unidades.'
            )

        return quantity
