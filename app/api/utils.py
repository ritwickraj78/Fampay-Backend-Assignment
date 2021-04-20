import os
from datetime import datetime, timedelta

import pytz
from django.db.models import Q
from googleapiclient.discovery import build

from api.models import MetaData, GoogleAPIKeys

from app.settings import NO_OF_KEYS


def get_videos_from_api(page_token=None):
    """
    A function to extract videos from the Youtube Data API
    :param page_token: The token for the page number of the videos
    :return: The response from the API
    """
    meta_data = MetaData.objects.first()
    print(meta_data.key_index)
    if not meta_data:
        meta_data = MetaData()
        meta_data.save()
    if meta_data.key_index == 0:
        print("All Keys Expired! Task Stopped. Please Try later")
        return {'stop_task': True}
    api_key = GoogleAPIKeys.objects.filter(Q(index=meta_data.key_index)).first()
    if api_key.last_expired:
        if api_key.last_expired.day != datetime.utcnow().day:
            usable_key = api_key.key
        else:
            meta_data.key_index = (meta_data.key_index + 1) % (NO_OF_KEYS + 1)
            meta_data.save()
            if meta_data.key_index == 0:
                print("All Keys Expired! Task Stopped. Please Try later")
                return {'stop_task': True}
            api_key = GoogleAPIKeys.objects.filter(Q(index=meta_data.key_index)).first()
            if api_key.last_expired.day != datetime.utcnow().day:
                print("All Keys Expired! Task Stopped. Please Try later")
                return {'stop_task': True}
            usable_key = api_key.key
    else:
        usable_key = api_key.key
    API_KEY = usable_key
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
        print(response)
    except Exception as e:
        if e.status_code == 403:
            api_key.last_expired = datetime.utcnow()
            meta_data.key_index = (meta_data.key_index + 1) % (NO_OF_KEYS + 1)
            meta_data.save()
            api_key.save()
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
