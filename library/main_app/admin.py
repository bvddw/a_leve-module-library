from django.contrib import admin
from .models import MyUser
from genres.models import Genre
from authors.models import Author
from books.models import Book
from borrow_requests.models import BorrowRequestModel

admin.site.register(MyUser)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BorrowRequestModel)
