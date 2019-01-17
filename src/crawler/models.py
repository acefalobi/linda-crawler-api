import uuid

from django.db import models


class Article(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=1000)
    url = models.CharField(max_length=1000, unique=True)
    image_url = models.CharField(max_length=1000)
    snippet = models.TextField()

    log_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


