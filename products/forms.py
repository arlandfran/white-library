from django import forms

from .models import Product, Category
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names

        for field in self.fields:
            if field == 'sku':
                placeholder = field.upper()
            elif self.fields[field].required:
                placeholder = field.replace('_', ' ').title() + '*'
            else:
                placeholder = field.replace('_', ' ').title()
            self.fields[field].widget.attrs['placeholder'] = placeholder
