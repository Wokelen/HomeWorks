from rest_framework.exceptions import ValidationError


def val_not_published(value):
    if value:
        raise ValidationError("Нельзя создавать опубликованные объявления")

