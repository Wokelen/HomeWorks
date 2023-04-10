from rest_framework import routers

from ads.views.cat import CatViewSet

router = routers.SimpleRouter()
router.register('', CatViewSet)
urlpatterns = router.urls
