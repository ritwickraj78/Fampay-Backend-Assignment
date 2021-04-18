# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
from datetime import datetime, timezone

from googleapiclient.discovery import build


def print_hi():
    DEVELOPER_KEY = os.environ['API_KEY']
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"
    try:
        youtube_object = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                               developerKey=DEVELOPER_KEY)
        search_keyword = youtube_object.search().list(q="cats",
                                                      part="id, snippet",
                                                      maxResults=50,
                                                      publishedAfter="2021-01-01T00:00:00Z").execute()

        results = search_keyword.get("items", [])
    except:
        return {}
    return results


if __name__ == '__main__':
    print(print_hi()[0])
    local_time = datetime.now(timezone.utc).astimezone()
    print(local_time.isoformat())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
