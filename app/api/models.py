from django.db import models


# Create your models here.
class YoutubeVideo(models.Model):
    """
    A Model to Store Individual Youtube Videos
    """
    video_id = models.CharField(primary_key=True, max_length=256)
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    published_date = models.DateTimeField()
    thumbnail_url = models.URLField()

    def __str__(self):
        return self.title


class GoogleAPIKeys(models.Model):
    """
    Model to store the List of API Keys
    """
    key = models.CharField(max_length=256)
    last_expired = models.DateTimeField(blank=True,null=True)
    index = models.IntegerField()


class MetaData(models.Model):
    """
    Model to store API Metadata
    """
    key_index = models.IntegerField(default=1)
