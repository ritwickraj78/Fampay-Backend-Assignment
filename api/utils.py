import os

from googleapiclient.discovery import build


def get_videos_from_api():
    API_KEY = os.environ['API_KEY']
    try:
        connection = build("youtube",
                           "v3",
                           developerKey=API_KEY)
        response = connection.search().list(q="cats",
                                            part="id, snippet",
                                            maxResults=50,
                                            publishedAfter="2020-01-01T00:00:00Z").execute()

        results = response.get("items", [])
    except:
        return []
    return results

