from django import forms
from .models import Genre


class CreateGenreForm(forms.Form):
    name = forms.CharField(label='Name', widget=forms.TextInput(
        attrs={
            "type": "text",
            "class": "form-control shadow",
            "id": "Name",
            "placeholder": "Name",
            "name": "name",
        }
    ))

    def clean(self):
        name = self.cleaned_data['name']
        if len(Genre.objects.filter(name=name)):
            self.add_error('name', 'Genre with this name already exist.')

    def create_genre(self):
        Genre.objects.create(**self.cleaned_data)


class UpdateGenreForm(forms.Form):
    name = forms.CharField(label='Name', widget=forms.TextInput(
        attrs={
            "type": "text",
            "class": "form-control shadow",
            "id": "Name",
            "placeholder": "Name",
            "name": "name",
        }
    ))

    def clean(self):
        name = self.cleaned_data['name']
        if len(Genre.objects.filter(name=name)):
            self.add_error('name', 'Genre with this name already exist.')