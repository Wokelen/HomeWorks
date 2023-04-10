import pytest

from rest_framework import status


@pytest.mark.django_db
def test_ad_create(client, user, category):
    data = {
        "author": user.username,
        "category": category.name,
        "name": "Стол из слэба и эпоксидной смолы",
        "price": 1234
    }
    expected_data = {
        "id": 1,
        "author": user.username,
        "category": category.name,
        "name": "Стол из слэба и эпоксидной смолы",
        "price": 1234,
        "description": None,
        "is_published": False,
        "image": None
    }
    response = client.post("/ads/", data=data)

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data == expected_data
