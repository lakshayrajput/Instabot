from Get_user_post_info import get_user_post_info
from Get_user_recent_post_id import get_user_recent_post_id
from constants import Base_url,App_Access_Token
from Friend_list import userName,friend_list
import requests





def like_a_post() :
    user_name = userName()
    post_id = get_user_recent_post_id(user_name)
    request_url = (Base_url + "media/%s/likes") % (post_id)
    payload = {"access_token": App_Access_Token}
    #print("Post request-url: "+request_url)
    post_a_like = requests.post(request_url,payload).json()
    if post_a_like ['meta']['code'] == 200 :
        print("Like was successful...")
    else :
        print("Your like was unsuccessful.Please try again...")

