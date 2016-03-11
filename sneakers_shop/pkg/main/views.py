from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'index.html'


class ContactsView(generic.TemplateView):
    template_name = 'contacts.html'


class AboutView(generic.TemplateView):
    template_name = 'about.html'


class CatalogView(generic.TemplateView):
    template_name = 'catalog.html'
