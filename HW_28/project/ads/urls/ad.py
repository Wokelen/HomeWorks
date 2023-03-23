from django.urls import path

from ads.views.ad import *

urlpatterns = [

    path('', AdListView.as_view(), name="all_category"),
    path('create/', AdCreateView.as_view(), name="category_create"),
    path('<int:pk>/', AdDetailView.as_view()),
    path('<int:pk>/update/', AdUpdateView.as_view()),
    path('<int:pk>/delete/', AdDeleteView.as_view()),
    path('<int:pk>/upload_image/', AdUploadImageView.as_view()),

]