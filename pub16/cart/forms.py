import email
from django import forms

QUANTITY_CHOISES = [(i, str(i)) for i in range(1, 11)]


class CartAddProduct(forms.Form):
    quantity = forms.TypedChoiceField(
        initial=1, choices=QUANTITY_CHOISES, coerce=int, label='Количество', widget=forms.HiddenInput)
    update = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput)


class CartUpdateProduct(forms.Form):
    quantity = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'number',
            'min': 0,
            'value': 1,
            'readonly': True,
        }))
    update = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput)


class DeliveyForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'placeholder': 'ФИО',
        'id': 'name-6797',
        'name': 'name',
        'class': 'u-border-1 u-border-grey-30 u-input u-input-rectangle',
        'required': ''
    }))

    table = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': 'Столик',
        'id': 'email-6797',
        'name': 'table',
        'class': 'u-border-1 u-border-grey-30 u-input u-input-rectangle',
        'required': ''
    }
    ))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'tel',
        'pattern': '\+?\d{0,3}[\s\(\-]?([0-9]{2,3})[\s\)\-]?([\s\-]?)([0-9]{3})[\s\-]?([0-9]{2})[\s\-]?([0-9]{2})',
        'placeholder': '+7 123 456 7890',
        'id': 'phone-6900',
        'name': 'phone',
        'class': 'u-border-1 u-border-grey-30 u-input u-input-rectangle',
        'required': ''
    }))
