from Get_user_id import get_user_id
from constants import Base_url, App_Access_Token
import requests





# -----get user latest post-id-----#
def get_user_recent_post_id(username):

    user_id = get_user_id(username)
    request_url = (Base_url + "users/%s/media/recent/?access_token=%s" % (user_id, App_Access_Token))
    #print("Get request url: " + request_url)
    user_info = requests.get(request_url).json()
    if user_info['meta']['code'] == 200:

        if len(user_info['data']):
            print("Comments on this post : %s" % (user_info['data'][0]['comments']['count']))

            return (user_info['data'][0]['id'])


        else:
            print("No info exist")
    else:
        print("Incorrect code..")
