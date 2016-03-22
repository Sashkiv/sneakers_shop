from django import forms
from django.db.models import Min, Max

from sneakers_shop.pkg.sneakers.models import Sneaker, Brand, SneakersSize


class QuiteModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def _check_values(self, value):
        try:
            value = frozenset(value)
        except TypeError:
            pass
        else:
            pks_for_del = []
            pks = self.queryset.values_list('pk', flat=True)
            for pk in value:
                try:
                    if int(pk) not in pks:
                        pks_for_del.append(pk)
                except (TypeError, ValueError):
                    pks_for_del.append(pk)
            value = list(value)
            for pk in pks_for_del:
                value.remove(pk)
        return super(QuiteModelMultipleChoiceField, self)._check_values(value)


class SneakersFilterForm(forms.Form):

    brand = QuiteModelMultipleChoiceField(
        queryset=Brand.objects.all(),
        required=False
    )
    gender = forms.ChoiceField(choices=Sneaker.GENDER, required=False)
    size = forms.IntegerField(required=False)
    price_from = forms.IntegerField(required=False)
    price_to = forms.IntegerField(required=False)

    def __init__(self, *args, **kwargs):
        super(SneakersFilterForm, self).__init__(*args, **kwargs)

        size_range = SneakersSize.objects.aggregate(Min('size'), Max('size'))
        self.fields['size'].min_value = size_range.get('size__min', 30)
        self.fields['size'].max_value = size_range.get('size__max', 50)

    def clean(self):
        cleaned_data = super(SneakersFilterForm, self).clean()
        keys_for_remove = []
        for k, v in cleaned_data.items():
            if v is None or v == '':
                keys_for_remove.append(k)

        for key in keys_for_remove:
            del cleaned_data[key]

        return cleaned_data
