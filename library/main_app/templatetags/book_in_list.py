from django import template

register = template.Library()


@register.inclusion_tag('book_view.html')
def display_books(book):
    return {'book': book}
