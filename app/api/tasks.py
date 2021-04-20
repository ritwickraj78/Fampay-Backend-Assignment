from asyncio import sleep

from celery import shared_task

from api.models import YoutubeVideo
from api.utils import get_videos_from_api, convert_time_to_unix


@shared_task
def populate_db(response):
    """
    A function which runs as a shared task on celery using RabbitMQ as a broker
    :param response: Gets a Response from the youtube api
    :return: The token for the next page in the API
    """
    if not response:
        return None
    results = response.get("items", [])
    token = response['nextPageToken'] if 'nextPageToken' in response else None
    for object in results:
        video_id = object['id']['videoId']
        thumbnail_url = object['snippet']['thumbnails']['medium']['url']
        title = object['snippet']['title'] if object['snippet']['title'] else None
        description = object['snippet']['description'] if object['snippet']['description'] else None
        published_date = convert_time_to_unix(object['snippet']['publishedAt']) if object['snippet'][
            'publishedAt'] else None
        try:
            video = YoutubeVideo(
                video_id=video_id,
                thumbnail_url=thumbnail_url,
                title=title,
                description=description,
                published_date=published_date,
            )
            video.save()
            print("object added")
        except Exception as e:
            print(e)
            print("Video Already in DB")
            continue
        sleep(1)
    return token


token = None

# Make an api call and populate the database every 30 seconds
while True:
    sleep(30)
    if not token:
        response = get_videos_from_api()
    else:
        response = get_videos_from_api(token)
    if 'stop_task' in response:
        break
    token = populate_db(response=response)
