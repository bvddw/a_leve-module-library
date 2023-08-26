from .models import Genre, Author


def authors(request):
    return {'authors': Author.objects.all()}


def genres(request):
    return {'genres': Genre.objects.all()}
