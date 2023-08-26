from datetime import timedelta
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView
from django.utils import timezone
from main_app.models import *
from main_app.forms import *


class ApproveRequestBookView(LoginRequiredMixin, View):
    model = BorrowRequestModel

    def get(self, request, id):
        bor_request = BorrowRequestModel.objects.get(id=id)
        bor_request.status = 2
        bor_request.approval_date = timezone.now().date()
        bor_request.save()

        return redirect('users:user_profile_view', username=request.user.username)


class DeclineRequestBookView(LoginRequiredMixin, View):
    model = BorrowRequestModel

    def get(self, request, id):
        bor_request = BorrowRequestModel.objects.get(id=id)
        bor_request.status = 5
        bor_request.save()

        return redirect('users:user_profile_view', username=request.user.username)


class TakeBookView(LoginRequiredMixin, View):
    model = BorrowRequestModel

    def get(self, request, id):
        borrow_request = self.model.objects.get(id=id)
        if borrow_request.status != 2:
            return redirect('books:book_detail_view', isbn=borrow_request.book.isbn)
        else:
            borrow_request.status = 3
            current_date = timezone.now().date()
            new_date = current_date + timedelta(weeks=2)
            borrow_request.due_date = new_date
            borrow_request.save()
            book = borrow_request.book
            book.available = False
            book.save()

        return redirect('users:user_profile_view', username=request.user.username)


class ReturnBookView(LoginRequiredMixin, View):
    model = BorrowRequestModel

    def get(self, request, id):
        borrow_request = self.model.objects.get(id=id)
        if borrow_request.status != 3:
            return redirect('books:book_detail_view', isbn=borrow_request.book.isbn)
        else:
            borrow_request.status = 4
            current_date = timezone.now().date()
            if current_date > borrow_request.due_date:
                borrow_request.overdue = True
            borrow_request.complete_date = current_date
            borrow_request.save()
            book = borrow_request.book
            book.available = True
            book.save()

        return redirect('users:user_profile_view', username=request.user.username)


class BorrowHistoryView(ListView):
    model = BorrowRequestModel
    template_name = 'borrow_history_view.html'
    context_object_name = 'borrow_requests'

    def get_queryset(self):
        return self.model.objects.all().order_by('status')