from django import forms
from .models import Good


class BaseOrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class GoodItemForm(forms.ModelForm):

    class Meta:
        model = Good
        fields = '__all__'
