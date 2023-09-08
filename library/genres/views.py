from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import DetailView, CreateView
from django.urls import reverse
from books.models import Book
from .models import Genre
from .forms import CreateGenreForm, UpdateGenreForm


class GenreDetailView(DetailView):
    model = Genre
    template_name = "genre_detail_view.html"
    context_object_name = 'genre'

    def get_object(self, queryset=None):
        name = self.kwargs['name']
        return get_object_or_404(Genre, name=name)

    def get_context_data(self, **kwargs):
        genre = self.get_object()
        books = Book.objects.filter(genres=genre)
        context = super().get_context_data(**kwargs)
        context['books'] = books
        return context


class CreateGenreView(CreateView):
    model = Genre
    template_name = 'create_genre_view.html'

    def get(self, request):
        if not request.user.is_librarian and not request.user.is_staff:
            url = reverse('main_view')
            return HttpResponseRedirect(url)
        form = CreateGenreForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CreateGenreForm(request.POST)
        if form.is_valid():
            form.create_genre()
            url = reverse('main_view')
            return HttpResponseRedirect(url)
        return render(request, self.template_name, {'form': form})


class UpdateGenreView(View):
    template_name = 'update_genre_view.html'

    def get(self, request, name):
        if not request.user.is_librarian and not request.user.is_staff:
            url = reverse('main_view')
            return HttpResponseRedirect(url)
        genre = Genre.objects.get(name=name)
        form = UpdateGenreForm({'name': genre.name})

        return render(request, self.template_name, {'form': form})

    def post(self, request, name):
        genre = Genre.objects.get(name=name)
        form = UpdateGenreForm(request.POST)

        if form.is_valid():
            genre.name = form.cleaned_data['name']
            genre.save()
            url = reverse('main_view')
            return HttpResponseRedirect(url)

        return render(request, self.template_name, {'form': form})


class DeleteGenreView(View):
    def get(self, request, name):
        if not request.user.is_librarian and not request.user.is_staff:
            url = reverse('main_view')
            return HttpResponseRedirect(url)
        genre = Genre.objects.get(name=name)
        genre.delete()
        url = reverse('main_view')
        return HttpResponseRedirect(url)