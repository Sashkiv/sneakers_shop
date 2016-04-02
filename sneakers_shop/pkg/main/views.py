from django.views import generic
from django.utils.translation import ugettext_lazy as _


class IndexView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['title'] = _("Головна. Інтернет-магазин спортивного "
                             "оригінального взуття Sport People.")
        return context


class ContactsView(generic.TemplateView):
    template_name = 'contacts.html'

    def get_context_data(self, **kwargs):
        context = super(ContactsView, self).get_context_data(**kwargs)
        context['title'] = _("Контактна інформація. Інтернет-магазин "
                             "спортивного оригінального взуття Sport People")
        return context


class AboutView(generic.TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['title'] = _("Про нас. Інтернет-магазин спортивного "
                             "оригінального взуття Sport People")
        return context


class CatalogView(generic.TemplateView):
    template_name = 'catalog.html'

    def get_context_data(self, **kwargs):
        context = super(CatalogView, self).get_context_data(**kwargs)
        context['title'] = _("Каталог. Вибери свій товар. Інтернет-магазин "
                             "спортивного оригінального взуття Sport People")
        return context


class DeliveryView(generic.TemplateView):
    template_name = 'delivery.html'

    def get_context_data(self, **kwargs):
        context = super(DeliveryView, self).get_context_data(**kwargs)
        context['title'] = _("Доставка. Інтернет-магазин спортивного "
                             "оригінального взуття Sport People")
        return context


class GoogleVerification(generic.TemplateView):
    template_name = 'google4346c5c573bda2ea.html'
