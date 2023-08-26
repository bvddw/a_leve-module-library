from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError

from .models import MyUser


class LoginUserForm(forms.Form):
    username = forms.CharField(label="Username", widget=forms.TextInput(
        attrs={
            "type": "text",
            "class": "form-control shadow",
            "id": "username",
            "placeholder": "Username",
            "name": "username"
        }
    ))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={
            "type": "password",
            "class": "form-control shadow",
            "id": "password",
            "placeholder": "Password",
            "name": "password"
        }
    ))

    def clean(self):
        if not authenticate(**self.cleaned_data):
            raise ValidationError('Incorrect username or password.')


class RegistrateUserForm(forms.Form):
    username = forms.CharField(label="Username", widget=forms.TextInput(
        attrs={
            "type": "text",
            "class": "form-control shadow",
            "id": "username",
            "placeholder": "Username",
            "name": "username"
        }
    ))
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(
        attrs={
            "type": "text",
            "class": "form-control shadow",
            "id": "First Name",
            "placeholder": "First Name",
            "name": "first_name"
        }
    ))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(
        attrs={
            "type": "text",
            "class": "form-control shadow",
            "id": "Last Name",
            "placeholder": "Last Name",
            "name": "last_name"
        }
    ))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={
            "type": "password",
            "class": "form-control shadow",
            "id": "password",
            "placeholder": "Password",
            "name": "password"
        }
    ))
    confirm_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(
        attrs={
            "type": "password",
            "class": "form-control shadow",
            "id": "confirmPassword",
            "placeholder": "Confirm Password",
            "name": "confirm_password"
        }
    ))

    def create_user(self):
        del self.cleaned_data["confirm_password"]
        MyUser.objects.create_user(**self.cleaned_data)

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            MyUser.objects.get(username=username)
            raise ValidationError("User with this username already registered.")
        except MyUser.DoesNotExist:
            return username

    def clean(self):
        password = self.cleaned_data["password"]
        confirm_password = self.cleaned_data["confirm_password"]
        if password != confirm_password:
            self.add_error("password", "Does not match")
            self.add_error("confirm_password", "Does not match")


class SetUserDataForm(forms.Form):
    first_name = forms.CharField(label="First name", required=False, widget=forms.TextInput(
        attrs={
            "type": "text",
            "class": "form-control shadow",
            "id": "first name",
            "placeholder": "First name",
            "name": "first_name",
        }
    ))
    last_name = forms.CharField(label="Last name", required=False, widget=forms.TextInput(
        attrs={
            "type": "text",
            "class": "form-control shadow",
            "id": "last name",
            "placeholder": "Last name",
            "name": "last_name"
        }
    ))
    email = forms.CharField(label='Email', widget=forms.TextInput(
        attrs={
            "type": "email",
            "class": "form-control shadow",
            "id": "email",
            "placeholder": "Email",
            "name": "email"
        }
    ))

    def update_data(self, username):
        user = MyUser.objects.get(username=username)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.save()


class SetNewPassword(forms.Form):
    old_password = forms.CharField(label="Old password", widget=forms.PasswordInput(
        attrs={
            "type": "password",
            "class": "form-control shadow",
            "id": "oldPassword",
            "placeholder": "Old password",
            "name": "old_password"
        }
    ))
    new_password = forms.CharField(label="New password", widget=forms.PasswordInput(
        attrs={
            "type": "password",
            "class": "form-control shadow",
            "id": "newPassword",
            "placeholder": "New password",
            "name": "new_password"
        }
    ))
    confirm_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(
        attrs={
            "type": "password",
            "class": "form-control shadow",
            "id": "confirmPassword",
            "placeholder": "Confirm Password",
            "name": "confirm_password"
        }
    ))

    def update_data(self, username):
        user = MyUser.objects.get(username=username)
        new_password = self.cleaned_data["new_password"]
        user.set_password(new_password)
        user.save()

    def clean(self):
        old_password = self.cleaned_data["old_password"]
        username = self.initial.get("username")  # Assume you pass the username when initializing the form
        try:
            user = MyUser.objects.get(username=username)
        except MyUser.DoesNotExist:
            raise forms.ValidationError("User does not exist")

        if not user.check_password(old_password):
            self.add_error("old_password", "Incorrect old password")
        new_password = self.cleaned_data["new_password"]
        confirm_password = self.cleaned_data["confirm_password"]
        if new_password != confirm_password:
            self.add_error("new_password", "Does not match")
            self.add_error("confirm_password", "Does not match")