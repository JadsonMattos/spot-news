from django.core.exceptions import ValidationError


def validate_title(value):
    words = value.split()
    if len(words) < 2:
        raise ValidationError('O título deve conter pelo menos 2 palavras.')
