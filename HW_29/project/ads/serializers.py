from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer
from users.models import User

from ads.models import Ad, Category
from users.serializers import UserDetailSerializer


class AdSerializer(ModelSerializer):
    class Meta:
        model = Ad
        fields = "__all__"


class AdListSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field="username", queryset=User.objects.all())
    category = SlugRelatedField(slug_field="name", queryset=Category.objects.all())

    class Meta:
        model = Ad
        fields = "__all__"


class AdDetailSerializer(ModelSerializer):
    author = UserDetailSerializer()
    category = SlugRelatedField(slug_field="name", queryset=Category.objects.all())

    class Meta:
        model = Ad
        fields = "__all__"
