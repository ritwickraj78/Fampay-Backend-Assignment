import os
from datetime import datetime, timedelta

import pytz
from googleapiclient.discovery import build


def get_videos_from_api(page_token=None):
    """
    A function to extract videos from the Youtube Data API
    :param page_token: The token for the page number of the videos
    :return: The response from the API
    """
    API_KEY = os.environ['API_KEY']
    try:
        connection = build("youtube",
                           "v3",
                           developerKey=API_KEY)
        date = datetime.utcnow() - timedelta(days=2)
        if page_token:
            response = connection.search().list(q="cats",
                                                part="id, snippet",
                                                maxResults=20,
                                                order='date',
                                                pageToken=page_token,
                                                type="video",
                                                publishedAfter=convert_time_to_rfc(date)).execute()
        else:
            response = connection.search().list(q="cats",
                                                part="id, snippet",
                                                maxResults=2,
                                                order='date',
                                                type="video",
                                                publishedAfter=convert_time_to_rfc(date)).execute()
    except Exception as e:
        print(e)
        return {}
    return response


def convert_time_to_unix(time):
    """
    Convert RFC 3339 String to Datetime Object
    :param time: timestamp in string
    :return: Datetime Object
    """
    try:
        time_obj = datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ")
    except:
        return None
    return time_obj


def convert_time_to_rfc(time):
    """
    Convert Datetime Object to RFC3339 String
    :param time: Datetime Object
    :return: String
    """
    try:
        time_str = datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ")
    except:
        return None
    return time_str
