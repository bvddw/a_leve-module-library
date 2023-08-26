from django.views.generic import TemplateView, ListView
from main_app.models import *
from main_app.forms import *


class MainView(ListView):
    paginate_by = 2
    template_name = 'index.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.all()


class AboutView(TemplateView):
    template_name = "about.html"