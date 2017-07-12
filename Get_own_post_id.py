from constants import Base_url,App_Access_Token
import requests
from datetime import datetime, timedelta
import urllib

def get_own_post_id() :
    request_url = (Base_url + "users/self/media/recent/?access_token=%s") % (App_Access_Token)
    #print("Get request url: %s"%(request_url))
    own_media = requests.get(request_url).json()
    #print(own_media)
    if own_media ['meta']['code'] == 200 :
        if len(own_media['data']) :

            return (own_media['data'][0]['id'])
        else:
            print("Post does not exist")
    else :
        print("Status code is wrong")
