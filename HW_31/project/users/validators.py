import datetime

from rest_framework.exceptions import ValidationError


def check_birth_date(birth_date):
    today = datetime.date.today()
    age = (today.year - birth_date.year -1) + ((today.month, today.day) >= (birth_date.month, birth_date.day))
    if age < 9:
        raise ValidationError(f" {age} -слишком молодой возраст для регистрации")


def check_email(email):
    if "rambler.ru" in email:
        raise ValidationError("с домена rambler регистрация запрещена")
