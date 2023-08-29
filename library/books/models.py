from django.db import models
from main_app.models import MyUser
from genres.models import Genre
from authors.models import Author


class Book(models.Model):
    title = models.CharField(max_length=255, unique=True)
    summary = models.TextField()
    isbn = models.CharField(max_length=13, unique=True)
    is_available = models.BooleanField(default=True)
    published_date = models.DateField()
    publisher = models.CharField(max_length=255)
    borrower = models.OneToOneField(MyUser, on_delete=models.SET_NULL, null=True, blank=True)
    genres = models.ManyToManyField(Genre, blank=True)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title
