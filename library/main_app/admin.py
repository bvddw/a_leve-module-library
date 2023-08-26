from django.contrib import admin
from .models import MyUser, Genre, Author, Book, BorrowRequestModel

admin.site.register(MyUser)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BorrowRequestModel)
