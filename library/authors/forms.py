from django import forms
from main_app.models import Author


class CreateAuthorForm(forms.Form):
    name = forms.CharField(label='Name', widget=forms.TextInput(
        attrs={
            "type": "text",
            "class": "form-control shadow",
            "id": "Name",
            "placeholder": "Name",
            "name": "name",
        }
    ))
    bio = forms.CharField(label='Bio', widget=forms.TextInput(
        attrs={
            "type": "text",
            "class": "form-control shadow",
            "id": "Bio",
            "placeholder": "Bio",
            "name": "bio",
        }
    ))

    def clean(self):
        name = self.cleaned_data['name']
        if len(Author.objects.filter(name=name)):
            self.add_error('name', 'Author with this name already exist.')

    def create_author(self):
        Author.objects.create(**self.cleaned_data)


class UpdateAuthorForm(forms.Form):
    name = forms.CharField(label='Name', widget=forms.TextInput(
        attrs={
            "type": "text",
            "class": "form-control shadow",
            "id": "Name",
            "placeholder": "Name",
            "name": "name",
        }
    ))
    bio = forms.CharField(label='Bio', widget=forms.TextInput(
        attrs={
            "type": "text",
            "class": "form-control shadow",
            "id": "Bio",
            "placeholder": "Bio",
            "name": "bio",
        }
    ))

    def clean(self):
        name = self.cleaned_data['name']
        if len(Author.objects.filter(name=name)):
            self.add_error('name', 'Author with this name already exist.')
