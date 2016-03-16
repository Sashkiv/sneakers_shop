from django.views import generic

from sneakers_shop.pkg.sneakers.models import Sneaker
from sneakers_shop.pkg.sneakers.forms import SneakersFilterForm


class SneakersListView(generic.ListView):

    queryset = Sneaker.objects.filter(is_ready=True)
    paginate_by = 6

    def get_context_data(self, **kwargs):
        form = SneakersFilterForm(self.request.GET)
        kwargs['form'] = form
        return super(SneakersListView, self).get_context_data(**kwargs)

    def get(self, request, *args, **kwargs):

        form = SneakersFilterForm(request.GET)
        form.is_valid()
        self.queryset = self.queryset.filter(**form.clean())
        return super(SneakersListView, self).get(request, *args, **kwargs)


class SneakersDetailView(generic.DetailView):

    def get_queryset(self):
        return Sneaker.objects.filter(is_ready=True)
