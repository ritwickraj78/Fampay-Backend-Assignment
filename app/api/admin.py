from django.contrib import admin

# Register your models here.
from api.models import YoutubeVideo, MetaData, GoogleAPIKeys

admin.site.register(YoutubeVideo)
admin.site.register(GoogleAPIKeys)
admin.site.register(MetaData)
