from django.views import View
from django.views.generic import DetailView, CreateView
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from books.models import Book
from .models import Author
from .forms import CreateAuthorForm, UpdateAuthorForm


class AuthorDetailView(DetailView):
    model = Author
    template_name = "author_detail_view.html"
    context_object_name = 'author'

    def get_object(self, queryset=None):
        name = self.kwargs['name']
        return get_object_or_404(Author, name=name)

    def get_context_data(self, **kwargs):
        author = self.get_object()
        books = Book.objects.filter(authors=author)
        context = super().get_context_data(**kwargs)
        context['books'] = books
        return context


class CreateAuthorView(CreateView):
    model = Author
    template_name = 'create_author_view.html'

    def get(self, request):
        if not request.user.is_librarian and not request.user.is_staff:
            url = reverse('main_view')
            return HttpResponseRedirect(url)
        form = CreateAuthorForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CreateAuthorForm(request.POST)
        if form.is_valid():
            form.create_author()
            url = reverse('main_view')
            return HttpResponseRedirect(url)
        return render(request, self.template_name, {'form': form})


class UpdateAuthorView(View):
    template_name = 'update_author_view.html'

    def get(self, request, name):
        if not request.user.is_librarian and not request.user.is_staff:
            url = reverse('main_view')
            return HttpResponseRedirect(url)
        author = Author.objects.get(name=name)
        form = UpdateAuthorForm({'name': author.name, 'bio': author.bio})

        return render(request, self.template_name, {'form': form})

    def post(self, request, name):
        author = Author.objects.get(name=name)
        form = UpdateAuthorForm(request.POST)

        if form.is_valid():
            author.name = form.cleaned_data['name']
            author.bio = form.cleaned_data['bio']
            author.save()
            url = reverse('main_view')
            return HttpResponseRedirect(url)

        return render(request, self.template_name, {'form': form})


class DeleteAuthorView(View):
    def get(self, request, name):
        if not request.user.is_librarian and not request.user.is_staff:
            url = reverse('main_view')
            return HttpResponseRedirect(url)
        author = Author.objects.get(name=name)
        author.delete()
        url = reverse('main_view')
        return HttpResponseRedirect(url)