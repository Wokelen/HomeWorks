from django.urls import path

from ads.views.cat import *

urlpatterns = [
    path('', CatListView.as_view(), name="all_category"),
    path('create/', CatCreateView.as_view(), name="category_create"),
    path('<int:pk>', CatDetailView.as_view(), name="category_detail"),
    path('<int:pk>/update/', CatUpdateView.as_view()),
    path('<int:pk>/delete/', CatDeleteView.as_view()),

]