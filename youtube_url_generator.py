"""Generates the url of the latest video uploaded on Youtube"""

import requests
import json
from settings import *


# Gets response
response = requests.get(Youtube_base_url)
r = response.status_code

# Generates the latest video url
try:
    if r == 200:
        json_data = json.loads(response.text)

        # Retrieves video title
        video_title = (json_data['items'][0]['snippet']['title'])

        # Retrieves video_id for video url
        video_id = (json_data['items'][0]['snippet']['resourceId']['videoId'])
        video_url = Youtube_watch_url + video_id

        # The post to be shared
        video_post = video_title + '\n' + video_url
    else:
        raise Exception(r)
except Exception as e:
    print(e)
