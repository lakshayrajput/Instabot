from Get_user_id import get_user_id
from Friend_list import userName,friend_list
from constants import Base_url,App_Access_Token
import requests
import urllib
from PIL import Image


def get_all_posts() :
    username = userName()

    user_id = get_user_id(username)
    request_url = (Base_url + "users/%s/media/recent/?access_token=%s" % (user_id, App_Access_Token))
    #print("Get request url: " + request_url)
    user_info = requests.get(request_url).json()
    if user_info['meta']['code'] == 200:

        if len(user_info['data']):
            pic_no = 0
            for post in range(0,len(user_info['data'])):
                pic_no = post + 1

                pic_id = user_info['data'][post]['id']
                image_name =username +str(pic_no)+".jpg"
                image_url = user_info['data'][post]['images']['standard_resolution']['url']
                urllib.urlretrieve(image_url,image_name)
                original = Image.open(image_name)
                original.show()
            print("Total no of saved pics: "+str(pic_no))




        else:
            print("No info exist")
    else:
        print("Incorrect code..")



