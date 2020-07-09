import facebook
from youtube_url_generator import video_title, video_url

def post_new_video():
        post = {
            'message': video_title,
            'link': video_url,
        }
        graph = facebook.GraphAPI(access_token='', version='3.1')
        
        api_request = graph.put_object(
            parent_object='me',
            connection_name='feed',
            message=post['message'],
            link=post['link']
        )

        if api_request == True:
            table.update({'sent': True}, Query().link == post['link'])
