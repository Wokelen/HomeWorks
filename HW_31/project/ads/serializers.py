from rest_framework.fields import BooleanField
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from ads.validators import val_not_published
from users.models import User

from ads.models import Ad, Category, Selection
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


class AdCreateSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field="username", queryset=User.objects.all())
    category = SlugRelatedField(slug_field="name", queryset=Category.objects.all())
    is_published = BooleanField(validators=[val_not_published], required=False)

    class Meta:
        model = Ad
        fields = "__all__"


class AdDetailSerializer(ModelSerializer):
    author = UserDetailSerializer()
    category = SlugRelatedField(slug_field="name", queryset=Category.objects.all())

    class Meta:
        model = Ad
        fields = "__all__"


class SelectionSerializer(ModelSerializer):

    class Meta:
        model = Selection
        fields = "__all__"


class SelectionDetailSerializer(ModelSerializer):
    items = AdSerializer(many=True)

    class Meta:
        model = Selection
        fields = "__all__"


class SelectionListSerializer(ModelSerializer):
    owner = SlugRelatedField(slug_field="username", queryset=User.objects.all())

    class Meta:
        model = Selection
        fields = ["owner", "name"]
        

class SelectionCreateSerializer(ModelSerializer):
    owner = SlugRelatedField(slug_field="username", read_only=True)

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["owner"] = request.user
        return super().create(validated_data)

    class Meta:
        model = Selection
        fields = "__all__"


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"
