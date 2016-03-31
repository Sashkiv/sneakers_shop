from django.views import generic
from django.utils.translation import ugettext_lazy as _


class IndexView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['title'] = _("Головна")
        return context


class ContactsView(generic.TemplateView):
    template_name = 'contacts.html'

    def get_context_data(self, **kwargs):
        context = super(ContactsView, self).get_context_data(**kwargs)
        context['title'] = _("Контактна інформація")
        return context


class AboutView(generic.TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['title'] = _("Про нас")
        return context


class CatalogView(generic.TemplateView):
    template_name = 'catalog.html'

    def get_context_data(self, **kwargs):
        context = super(CatalogView, self).get_context_data(**kwargs)
        context['title'] = _("Каталог. Вибери свій товар.")
        return context


class DeliveryView(generic.TemplateView):
    template_name = 'delivery.html'

    def get_context_data(self, **kwargs):
        context = super(DeliveryView, self).get_context_data(**kwargs)
        context['title'] = _("Доставка")
        return context


class GoogleVerification(generic.TemplateView):
    template_name = 'google4346c5c573bda2ea.html'

