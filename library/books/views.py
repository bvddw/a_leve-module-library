from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views import View
from django.views.generic import DetailView, CreateView
from main_app.models import *
from .forms import *


class BookDetailView(DetailView):
    model = Book
    template_name = "book_detail_view.html"
    context_object_name = 'book'

    def get_object(self, queryset=None):
        isbn = self.kwargs['isbn']
        return get_object_or_404(Book, isbn=isbn)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            if len(BorrowRequestModel.objects.filter(borrower=self.request.user, book=self.get_object())):
                context['bor_request'] = BorrowRequestModel.objects.get(borrower=self.request.user, book=self.get_object())
        return context


class RequestBookView(LoginRequiredMixin, View):
    model = BorrowRequestModel

    def get(self, request, isbn):
        user = request.user
        book = Book.objects.get(isbn=isbn)
        if len(BorrowRequestModel.objects.filter(borrower=user, book=book)):
            return redirect('users:user_profile_view', username=user.username)
        self.model.objects.create(book=book, borrower=user, request_date=timezone.now().date())

        return redirect('users:user_profile_view', username=user.username)


class CreateBookView(CreateView):
    model = Book
    template_name = 'create_book_view.html'

    def get(self, request):
        if not request.user.is_librarian and not request.user.is_staff:
            url = reverse('main_view')
            return HttpResponseRedirect(url)
        form = CreateBookForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CreateBookForm(request.POST)
        if form.is_valid():
            form.create_book()
            url = reverse('main_view')
            return HttpResponseRedirect(url)
        return render(request, self.template_name, {'form': form})


class UpdateBookView(View):
    template_name = 'update_book_view.html'

    def get(self, request, isbn):
        if not request.user.is_librarian and not request.user.is_staff:
            url = reverse('main_view')
            return HttpResponseRedirect(url)
        book = Book.objects.get(isbn=isbn)
        details = {
            'title': book.title,
            'summary': book.summary,
            'published_date': book.published_date,
            'publisher': book.publisher,
            'genres': book.genres.all(),
            'authors': book.authors.all(),
            'borrower': book.borrower,
        }
        form = UpdateBookForm(initial=details)

        return render(request, self.template_name, {'form': form})

    def post(self, request, isbn):
        book = Book.objects.get(isbn=isbn)
        form = UpdateBookForm(request.POST)

        if form.is_valid():
            form.update_book(book)
            url = reverse('main_view')
            return HttpResponseRedirect(url)

        return render(request, self.template_name, {'form': form})


class DeleteBookView(View):
    def get(self, request, isbn):
        if not request.user.is_librarian and not request.user.is_staff:
            url = reverse('main_view')
            return HttpResponseRedirect(url)
        book = Book.objects.get(isbn=isbn)
        book.delete()
        url = reverse('main_view')
        return HttpResponseRedirect(url)