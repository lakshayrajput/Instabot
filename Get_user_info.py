from constants import Base_url,App_Access_Token
from Get_user_id import get_user_id

import requests




def get_user_info(username) :
    own_id = get_user_id(username)
    request_url = (Base_url+"users/%s/?access_token=%s")%(own_id,App_Access_Token)
    #print("Get request: "+request_url)
    own_info = requests.get(request_url).json()
    if own_info ['meta']['code'] == 200 :
        if len(own_info['data']) :
            print("User-name: %s"%(own_info['data']['username']))
            print("Total media: %s" % (own_info['data']['counts']['media']))
            print("Total followers: %s" % (own_info['data']['counts']['followed_by']))
            print("following: %s" % (own_info['data']['counts']['follows']))

        else:
            print("No info exist")
    else:
        print("incorrect code..")