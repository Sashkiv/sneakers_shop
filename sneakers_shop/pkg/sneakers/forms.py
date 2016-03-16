from django import forms

from sneakers_shop.pkg.sneakers.models import Sneaker


class SneakersFilterForm(forms.ModelForm):
    class Meta:
        model = Sneaker
        fields = ['brand', 'gender', ]

    def __init__(self, *args, **kwargs):
        super(SneakersFilterForm, self).__init__(*args, **kwargs)
        self.fields['brand'].required = False
        self.fields['gender'].required = False

    def clean(self):
        cleaned_data = super(SneakersFilterForm, self).clean()
        keys_for_remove = []
        for k, v in cleaned_data.items():
            if v is None or v == '':
                keys_for_remove.append(k)

        for key in keys_for_remove:
            del cleaned_data[key]

        return cleaned_data
