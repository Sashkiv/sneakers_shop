from django.views import generic

from sneakers_shop.pkg.sneakers.models import Sneaker
from sneakers_shop.pkg.sneakers.forms import SneakersFilterForm


class SneakersListView(generic.ListView):

    queryset = Sneaker.objects.filter(is_ready=True)

    def get(self, request, *args, **kwargs):

        form = SneakersFilterForm(request.GET)
        if form.is_valid():
            self.queryset = self.queryset.filter(**form.clean())
        return super(SneakersListView, self).get(request, *args, **kwargs)


class SneakersDetailView(generic.DetailView):

    def get_queryset(self):
        return Sneaker.objects.filter(is_ready=True)
