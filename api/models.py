from django.db import models


# Create your models here.
class YoutubeVideo(models.Model):
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    published_date = models.DateTimeField()
    thumbnail_url = models.URLField()

    def __str__(self):
        return self.title