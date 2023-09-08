from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, reverse
from django.views import View
from django.views.generic import DetailView
from .models import MyUser
from borrow_requests.models import BorrowRequestModel
from .forms import LoginUserForm, RegistrateUserForm, SetUserDataForm, SetNewPassword


class LoginUserView(LoginView):
    template_name = 'login_view.html'

    def get(self, request, **kwargs):
        form = LoginUserForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, **kwargs):
        form = LoginUserForm(request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is not None:
                login(request, user)
                url = reverse('main_view')
                return HttpResponseRedirect(url)
        return render(request, self.template_name, {'form': form})


class RegisterUserView(View):
    template_name = 'register_view.html'

    def get(self, request):
        form = RegistrateUserForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegistrateUserForm(request.POST)
        if form.is_valid():
            form.create_user()
            url = reverse('users:login_user_view')
            return HttpResponseRedirect(url)
        return render(request, self.template_name, {'form': form})


class LoginView(View):
    template_name = 'login_view.html'

    def get(self, request):
        form = LoginUserForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = LoginUserForm(request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is not None:
                login(request, user)
                url = reverse('users:profile_view', kwargs={'username': user.username})
                return HttpResponseRedirect(url)
        return render(request, self.template_name, {'form': form})


class LogoutUserView(View):
    def get(self, request):
        url = reverse('users:login_user_view')
        logout(request)
        return HttpResponseRedirect(url)


class UserProfileView(DetailView):
    model = MyUser
    template_name = "profile_user_view.html"
    context_object_name = 'user'

    def get_object(self, queryset=None):
        username = self.kwargs['username']
        return get_object_or_404(MyUser, username=username)

    def get_context_data(self, **kwargs):
        user = self.get_object()
        requests = BorrowRequestModel.objects.filter(borrower=user)
        context = super().get_context_data(**kwargs)
        context['requests'] = requests
        if user.is_librarian:
            context['lib_requests'] = BorrowRequestModel.objects.filter(status=1)
        return context


class SetUserDataView(LoginRequiredMixin, View):
    login_url = 'login_user'

    def get(self, request, username):
        if username != request.user.username:
            url = reverse('users:user_profile_view', kwargs={'username': request.user.username})
            return HttpResponseRedirect(url)
        user = get_object_or_404(MyUser, username=username)
        fields = {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email
        }
        form = SetUserDataForm(initial=fields)
        return render(request, 'set_data.html', {"form": form})

    def post(self, request, username):
        user = get_object_or_404(MyUser, username=username)
        form = SetUserDataForm(request.POST)
        if form.is_valid():
            form.update_data(username)

            url = reverse('users:user_profile_view', kwargs={'username': username})
            return HttpResponseRedirect(url)
        return render(request, 'set_data.html', {"form": form})


class SetUserPasswordView(LoginRequiredMixin, View):
    login_url = 'login_user'

    def get(self, request, username):
        form = SetNewPassword(initial={'username': username})
        return render(request, 'set_password.html', {"form": form})

    def post(self, request, username):
        user = get_object_or_404(MyUser, username=username)
        form = SetNewPassword(request.POST, initial={'username': username})
        if form.is_valid():
            form.update_data(username)

            url = reverse('users:password_changed_view')
            return HttpResponseRedirect(url)
        return render(request, 'set_password.html', {"form": form})


class PasswordChangedView(View):
    def get(self, request):
        return render(request, 'password_changed.html')
