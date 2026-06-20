from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'item_price', 'item_description', 'item_image']

        widgets = {
            'item_name': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-xl p-3 focus:ring-2 focus:ring-lime-500 focus:outline-none'
            }),
            'item_description': forms.Textarea(attrs={
                'class': 'w-full border border-gray-300 rounded-xl p-3 focus:ring-2 focus:ring-lime-500 focus:outline-none',
                'rows': 4
            }),
            'item_price': forms.NumberInput(attrs={
                'class': 'w-full border border-gray-300 rounded-xl p-3 focus:ring-2 focus:ring-lime-500 focus:outline-none'
            }),
            'item_image': forms.URLInput(attrs={
                'class': 'w-full border border-gray-300 rounded-xl p-3 focus:ring-2 focus:ring-lime-500 focus:outline-none'
            }),
        }