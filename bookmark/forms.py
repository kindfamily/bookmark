from django import forms
from .models import Bookmark


class BookmarkForm(forms.ModelForm):
    site_name = forms.CharField(label='사이트명')
    url = forms.CharField(label='주소')

    class Meta:
        model = Bookmark
        fields = ['site_name', 'url']
        # model에서 불러오지 않을 필드를 지정
        # fields = '__all__' 로 전체를 지정하수도 있음
