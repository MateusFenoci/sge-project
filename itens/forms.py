# itens/forms.py

from django import forms
from . import models

class ItemForm(forms.ModelForm):

    class Meta:
        model = models.Item
        fields = ['product', 'size']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'size': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'product': 'Produto',
            'size': 'Tamanho',
        }
