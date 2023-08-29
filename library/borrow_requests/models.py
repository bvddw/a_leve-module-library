from django.db import models
from main_app.models import MyUser
from books.models import Book


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
