from django.urls import path

from .views import *

urlpatterns = [
    path('', BookmarkList.as_view(), name='bookmark_list'),
    path('detail/<int:pk>/', BookmarkDetail.as_view(), name='bookmark_detail'),
    path('create/', BookmarkCreate.as_view(), name='bookmark_create'),
    path('update/<int:pk>/', BookmarkUpdate.as_view(), name='bookmark_update'),
    path('delete/<int:pk>/', BookmarkDelete.as_view(), name='bookmark_delete'),
]