from django import forms
from authors.models import Author


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
        try:
            author = Author.objects.get(name=name)
            self.add_error('name', 'Author with this name already exists.')
        except Author.DoesNotExist:
            pass

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
        try:
            author = Author.objects.get(name=name)
            self.add_error('name', 'Author with this name already exists.')
        except Author.DoesNotExist:
            pass
