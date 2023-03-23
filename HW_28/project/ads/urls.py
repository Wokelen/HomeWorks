from django.urls import path

from ads.views import *
from users.views import *

urlpatterns = [
    path('', main_view),
    path('cat/', CatListView.as_view(), name="all_category"),
    path('cat/create/', CatCreateView.as_view(), name="category_create"),
    path('cat/<int:pk>', CatDetailView.as_view(), name="category_detail"),
    path('cat/<int:pk>/update/', CatUpdateView.as_view()),
    path('cat/<int:pk>/delete/', CatDeleteView.as_view()),
    path('ad/', AdListView.as_view(), name="all_category"),
    path('ad/create/', AdCreateView.as_view(), name="category_create"),
    path('ad/<int:pk>/', AdDetailView.as_view()),
    path('ad/<int:pk>/update/', AdUpdateView.as_view()),
    path('ad/<int:pk>/delete/', AdDeleteView.as_view()),
    path('ad/<int:pk>/upload_image/', AdUploadImageView.as_view()),
    path('user/', UserListView.as_view()),
    path('user/create/', UserCreateView.as_view()),
    path('user/<int:pk>', UserDetailView.as_view()),
    path('user/<int:pk>/update/', UserUpdateView.as_view()),
    path('user/<int:pk>/delete/', UserDeleteView.as_view()),
]
