from django.urls import path

from crawler.views import ArticleView

urlpatterns = [
    path('', ArticleView.as_view(), name='article_view'),
]
