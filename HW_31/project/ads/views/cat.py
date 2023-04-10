

from django.http import JsonResponse


from rest_framework.viewsets import ModelViewSet

from ads.models import Category
from ads.serializers import CategorySerializer


def main_view(request):
    return JsonResponse({"status": "ok"})


class CatViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer




