from django.views import generic

from sneakers_shop.pkg.sneakers.models import Sneaker
from sneakers_shop.pkg.sneakers.forms import SneakersFilterForm


class SneakersListView(generic.ListView):

    queryset = Sneaker.objects.filter(is_ready=True)
    paginate_by = 9

    def filter(self, form_cleaned_data):
        brands = form_cleaned_data.get('brand')
        gender = form_cleaned_data.get('gender')
        size = form_cleaned_data.get('size')
        price_from = form_cleaned_data.get('price_from', 0)
        price_to = form_cleaned_data.get('price_to')

        qs = self.queryset.filter(price__gt=price_from)
        if price_to:
            qs = qs.filter(price__lt=price_to)
        if brands:
            qs = qs.filter(brand__in=brands)
        if gender:
            qs = qs.filter(gender=gender)
        if size:
            qs = qs.filter(sneakers_size__size=size)
        return qs

    def get(self, request, *args, **kwargs):

        form = SneakersFilterForm(request.GET)
        form.is_valid()
        self.queryset = self.filter(form.clean())
        kwargs['form'] = form
        print(form)
        return super(SneakersListView, self).get(request, *args, **kwargs)


class SneakersDetailView(generic.DetailView):

    def get_queryset(self):
        return Sneaker.objects.filter(is_ready=True)
