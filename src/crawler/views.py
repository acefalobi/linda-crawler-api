from rest_framework.response import Response
from rest_framework.views import APIView

from crawler.models import Article
from crawler.serializers import ArticleSerializer


class ArticleView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        queryset = Article.objects.all().order_by('-log_time')[:60]
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)

