from django.views import generic
from django.http.response import HttpResponse
from django.utils.translation import ugettext_lazy as _

from sneakers_shop.pkg.sneakers.models import Sneaker, PromoInfo, Order
from sneakers_shop.pkg.sneakers.forms import SneakersFilterForm, OrderForm


class SneakersCatalogView(generic.ListView):

    queryset = Sneaker.objects.filter(is_ready=True)
    paginate_by = 15
    template_name = 'sneakers/sneakers_catalog.html'

    def qs_filter(self, form_cleaned_data):
        brands = form_cleaned_data.get('brand')
        gender = form_cleaned_data.get('gender')
        size = form_cleaned_data.get('size')
        price_from = form_cleaned_data.get('price_from')
        price_to = form_cleaned_data.get('price_to')

        qs = self.queryset
        if price_from:
            qs = qs.filter(price__gt=price_from)
        if price_to:
            qs = qs.filter(price__lt=price_to)
        if brands:
            qs = qs.filter(brand__in=brands)
        if gender:
            qs = qs.filter(gender=gender)
        if size:
            qs = qs.filter(sneakers_size__size=size)
        return qs

    def get_context_data(self, **kwargs):
        kwargs['form'] = self.form
        del self.form
        return super(SneakersCatalogView, self).get_context_data(**kwargs)

    def get(self, request, *args, **kwargs):

        form = SneakersFilterForm(request.GET)
        form.is_valid()
        self.queryset = self.qs_filter(form.clean())
        self.form = form
        return super(SneakersCatalogView, self).get(request, *args, **kwargs)


class SneakersListView(generic.ListView):

    def get_queryset(self):
        return Sneaker.objects.filter(is_ready=True)


class SneakersDetailView(generic.DetailView):

    def get_queryset(self):
        return Sneaker.objects.filter(is_ready=True)

    def get_context_data(self, **kwargs):
        context = super(SneakersDetailView, self).get_context_data(**kwargs)
        context['title'] = _("%(unit)s. Інтернет-магазин спортивного "
                             "оригінального взуття Sport People") % {
            'unit': self.object
        }
        context['order_form'] = OrderForm()
        return context


class PromoListView(generic.ListView):

    template_name = 'sneakers/promo_list.html'

    def get_queryset(self):
        return PromoInfo.objects.filter(is_ready=True)


class OrderView(generic.FormView):
    form_class = OrderForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        try:
            form.data._mutable = True
            form.data['sneakers'] = kwargs.get('pk')
        except AttributeError:
            pass
        return super(OrderView, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return HttpResponse(status=201)

    def form_invalid(self, form):
        return HttpResponse(status=400)
