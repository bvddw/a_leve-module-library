from django import forms
from django.utils import timezone
from main_app.models import *


class CreateBookForm(forms.Form):
    title = forms.CharField(label='Title', widget=forms.TextInput(
        attrs={
            "type": "text",
            "class": "form-control shadow",
            "id": "Title",
            "placeholder": "Title",
            "name": "title",
        }
    ))
    summary = forms.CharField(label='Summary', widget=forms.Textarea(
        attrs={
            "type": "text",
            "class": "form-control shadow",
            "id": "Summary",
            "placeholder": "Summary",
            "name": "summary",
        }
    ))
    isbn = forms.CharField(label='ISBN', widget=forms.TextInput(
        attrs={
            "type": "text",
            "class": "form-control shadow",
            "id": "ISBN",
            "placeholder": "ISBN",
            "name": "isbn",
        }
    ))
    published_date = forms.DateField(label='Published Date', widget=forms.DateInput(
        attrs={
            "type": "date",
            "class": "form-control shadow",
            "id": "Published Date",
            "placeholder": "Published Date",
            "name": "published_date",
        }
    ))
    publisher = forms.CharField(label='Publisher', widget=forms.TextInput(
        attrs={
            "type": "text",
            "class": "form-control shadow",
            "id": "Publisher",
            "placeholder": "Publisher",
            "name": "publisher",
        }
    ))
    genres = forms.ModelMultipleChoiceField(label='Genres', queryset=Genre.objects.all(), widget=forms.SelectMultiple(
        attrs={
            "class": "form-control shadow",
            "id": "Genres",
            "placeholder": "Genres",
            "name": "genres",
        }
    ))
    authors = forms.ModelMultipleChoiceField(label='Authors', queryset=Author.objects.all(), widget=forms.SelectMultiple(
        attrs={
            "class": "form-control shadow",
            "id": "Authors",
            "placeholder": "Authors",
            "name": "authors",
        }
    ))
    borrower = forms.ModelChoiceField(label='Borrower', queryset=MyUser.objects.all(), required=False, widget=forms.Select(
        attrs={
            "class": "form-control shadow",
            "id": "Borrower",
            "placeholder": "Borrower",
            "name": "borrower",
        }
    ))

    def clean(self):
        title = self.cleaned_data['title']
        if len(Book.objects.filter(title=title)):
            self.add_error('title', 'Book with this title already exist.')
        isbn = self.cleaned_data['isbn']
        if len(Book.objects.filter(isbn=isbn)):
            self.add_error('isbn', 'Book with this isbn already exist.')
        date = self.cleaned_data['published_date']
        if date > timezone.now().date():
            self.add_error('published_date', 'Unreal date for field "published date".')

    def create_book(self):
        genres = self.cleaned_data['genres']
        authors = self.cleaned_data['authors']

        book = Book.objects.create(
            title=self.cleaned_data['title'],
            summary=self.cleaned_data['summary'],
            isbn=self.cleaned_data['isbn'],
            published_date=self.cleaned_data['published_date'],
            publisher=self.cleaned_data['publisher'],
            is_available=True,
            borrower=self.cleaned_data['borrower']
        )

        book.genres.set(genres)
        book.authors.set(authors)
        book.save()


class UpdateBookForm(forms.Form):
    title = forms.CharField(label='Title', widget=forms.TextInput(
        attrs={
            "type": "text",
            "class": "form-control shadow",
            "id": "Title",
            "placeholder": "Title",
            "name": "title",
        }
    ))
    summary = forms.CharField(label='Summary', widget=forms.Textarea(
        attrs={
            "type": "text",
            "class": "form-control shadow",
            "id": "Summary",
            "placeholder": "Summary",
            "name": "summary",
        }
    ))
    published_date = forms.DateField(label='Published Date', widget=forms.DateInput(
        attrs={
            "type": "date",
            "class": "form-control shadow",
            "id": "Published Date",
            "placeholder": "Published Date",
            "name": "published_date",
        }
    ))
    publisher = forms.CharField(label='Publisher', widget=forms.TextInput(
        attrs={
            "type": "text",
            "class": "form-control shadow",
            "id": "Publisher",
            "placeholder": "Publisher",
            "name": "publisher",
        }
    ))
    genres = forms.ModelMultipleChoiceField(label='Genres', queryset=Genre.objects.all(), widget=forms.SelectMultiple(
        attrs={
            "class": "form-control shadow",
            "id": "Genres",
            "placeholder": "Genres",
            "name": "genres",
        }
    ))
    authors = forms.ModelMultipleChoiceField(label='Authors', queryset=Author.objects.all(), widget=forms.SelectMultiple(
        attrs={
            "class": "form-control shadow",
            "id": "Authors",
            "placeholder": "Authors",
            "name": "authors",
        }
    ))
    borrower = forms.ModelChoiceField(label='Borrower', queryset=MyUser.objects.all(), required=False, widget=forms.Select(
        attrs={
            "class": "form-control shadow",
            "id": "Borrower",
            "placeholder": "Borrower",
            "name": "borrower",
        }
    ))

    def update_book(self, book):
        book.title = self.cleaned_data['title']
        book.summary = self.cleaned_data['summary']
        book.published_date = self.cleaned_data['published_date']
        book.publisher = self.cleaned_data['publisher']
        book.borrower = self.cleaned_data['borrower']
        book.genres.set(self.cleaned_data['genres'])
        book.authors.set(self.cleaned_data['authors'])
        book.save()

    def clean(self):
        title = self.cleaned_data['title']
        if len(Book.objects.filter(title=title)):
            self.add_error('title', 'Book with this title already exist.')
        date = self.cleaned_data['published_date']
        if date > timezone.now().date():
            self.add_error('published_date', 'Unreal date for field "published date".')