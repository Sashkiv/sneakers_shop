from django import forms
from django.db.models import Min, Max
from django.utils.translation import ugettext_lazy as _

from sneakers_shop.pkg.sneakers.models import Sneaker, Brand, SneakersSize, \
    Order


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
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label=_('Бренд')
    )
    gender = forms.ChoiceField(
        choices=Sneaker.GENDER,
        required=False,
        label=_('Стать')
    )
    size = forms.FloatField(required=False, label=_('Розмір'))
    price_from = forms.IntegerField(required=False, label=_('Від ціни'))
    price_to = forms.IntegerField(required=False, label=_('До ціни'))

    def __init__(self, *args, **kwargs):
        super(SneakersFilterForm, self).__init__(*args, **kwargs)

        size_range = SneakersSize.objects.aggregate(Min('size'), Max('size'))
        _min = size_range.get('size__min', 30)
        _max = size_range.get('size__max', 50)
        self.fields['size'].min_value = _min
        self.fields['size'].max_value = _max
        self.fields['size'].widget.attrs.update({
            'min': _min,
            'max': _max,
            'step': 0.5,
            'class': 'form-control',
            'placeholder': _('Виберіть розмір')
        })
        self.fields['price_from'].widget.attrs.update({
            'step': 100,
            'class': 'form-control',
            'placeholder': _('Мінімальна ціна')
        })
        self.fields['price_to'].widget.attrs.update({
            'step': 100,
            'class': 'form-control',
            'placeholder': _('Максимальна ціна')
        })
        self.fields['gender'].widget.attrs.update({'class': 'form-control'})

    def clean(self):
        cleaned_data = super(SneakersFilterForm, self).clean()
        keys_for_remove = []
        for k, v in cleaned_data.items():
            if v is None or v == '':
                keys_for_remove.append(k)

        for key in keys_for_remove:
            del cleaned_data[key]

        return cleaned_data


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('sneakers', 'contact_info', 'comment', )
        widgets = {
            'comment': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
            'contact_info': forms.TextInput(
                attrs={
                    'placeholder': _('+380 98 765 43 21'),
                    'size': 40,
                }
            )
        }

    def clean_contact_info(self):
        symbols = ['+', ')', '(', ' ', '.', ',']
        data = self.cleaned_data.get('contact_info', '')
        for s in symbols:
            data = data.replace(s, '')
        if len(data) < 9:
            raise forms.ValidationError(_("Неправильний формат номера"))
        try:
            int(data)
        except ValueError:
            raise forms.ValidationError(_("Неправильний формат номера"))

        return self.cleaned_data.get('contact_info', '')
