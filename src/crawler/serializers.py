from rest_framework.serializers import ModelSerializer

from crawler.models import Article


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'url', 'image_url', 'snippet']
