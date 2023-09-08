from django.views.generic import TemplateView, ListView
from books.models import Book


class MainView(ListView):
    paginate_by = 3
    template_name = 'index.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.all()


class AboutView(TemplateView):
    template_name = "about.html"