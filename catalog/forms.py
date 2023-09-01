from django import forms

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'description', 'preview',)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        forbidden_words = ['слова', 'казино', 'криптовалюта',
                           'крипта', 'биржа', 'дешево', 'бесплатно',
                           'обман', 'полиция', 'радар']

        if cleaned_data in forbidden_words:
            raise forms.ValidationError('Это запрещенное слово')

        return cleaned_data


class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'
