from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    is_librarian = models.BooleanField(default=False)


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bio = models.TextField()

    def __str__(self):
        return self.name


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


class BorrowRequestModel(models.Model):
    PENDING = 1
    APPROVED = 2
    COLLECTED = 3
    COMPLETE = 4
    DECLINED = 5
    status_choices = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (COLLECTED, 'Collected'),
        (COMPLETE, 'Complete'),
        (DECLINED, 'Declined'),
    ]
    status = models.IntegerField(choices=status_choices, default=PENDING)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)  # if delete one book, then deleted all BorrowRequests
    borrower = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True, blank=True)
    overdue = models.BooleanField(default=False)
    request_date = models.DateField()
    approval_date = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    complete_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.borrower} : {self.book}'