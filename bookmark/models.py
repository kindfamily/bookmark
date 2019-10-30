from django.db import models
from django.urls import reverse_lazy
# Create your models here.
class Bookmark(models.Model):
    # 필드의 종류
    # 1. DB에 어떤 형태로 어떤 제약 사항으로 데이터를 저장하느냐
    # 2. 프론트에서 어떤 형태로 어떤 제약 사항을 가지고 입력을 받을 것이냐
    site_name = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return self.site_name + " : " + self.url

    # Todo : get_absolute_url method

    class Meta:
        ordering = ['site_name']

    def get_absolute_url(self):
        return reverse_lazy('bookmark_detail', args=[self.id])

# 모델의 내용을 데이터베이스 반영
# 2가지 명령어를 이용해서 ->