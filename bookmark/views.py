# 파이썬 빌트인 모듈

# 장고 모듈
from django.shortcuts import render
# 제네릭 뷰 : 웹 프로그래밍에서 많이 사용하는 기능을 미리 만들어 둔 형태
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
# 3rd party
# 우리가 만든거
from .models import Bookmark
# Create your views here.

# 제네릭 뷰를 사용하고 싶다면 클래스형 뷰를 사용합니다.
class BookmarkList(ListView):
    model = Bookmark
    template_name = 'bookmark/list.html'

class BookmarkDetail(DetailView):
    model = Bookmark
    template_name = 'bookmark/detail.html'

class BookmarkCreate(CreateView):
    model = Bookmark
    template_name = 'bookmark/create.html'
    fields = ['site_name','url']

class BookmarkUpdate(UpdateView):
    model = Bookmark
    template_name = 'bookmark/update.html'
    fields = ['site_name', 'url']

class BookmarkDelete(DeleteView):
    model = Bookmark
    template_name = 'bookmark/delete.html'
    success_url = '/'