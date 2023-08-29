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
        try:
            genre = Genre.objects.get(name=name)
            self.add_error('name', 'Genre with this name already exist.')
        except Genre.DoesNotExist:
            pass

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
        try:
            genre = Genre.objects.get(name=name)
            self.add_error('name', 'Genre with this name already exist.')
        except Genre.DoesNotExist:
            pass
