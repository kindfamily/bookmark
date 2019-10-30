from django.urls import path
from .views import *

app_name = 'bookmark'

urlpatterns = [
    path('', bookmark_list, name='bookmark_list'),
    path('new/', bookmark_new, name='bookmark_new'),
    path('edit/<int:pk>', bookmark_edit, name='bookmark_edit'),
    path('delete/<int:pk>', bookmark_delete, name='bookmark_delete'),
]