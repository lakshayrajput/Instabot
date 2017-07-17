from Get_user_id import get_user_id
from constants import Base_url,App_Access_Token
import requests
import urllib
from PIL import Image
from Friend_list import userName,friend_list





comment_list = []
post_id_list = []

def most_liked_user_post() :
    user_name = userName()
    user_id = get_user_id(user_name)
    request_url = (Base_url + "users/%s/media/recent/?access_token=%s" % (user_id, App_Access_Token))
    #print("Get request url: " + request_url)
    user_info = requests.get(request_url).json()
    if user_info['meta']['code'] == 200:

        if len(user_info['data']):
            for temp in range(0, len(user_info['data'])):
                post_id = user_info['data'][temp]['id']
                post_id_list.append(post_id)
                comment_count = user_info['data'][temp]['likes']['count']
                comment_list.append(comment_count)
            maximum = max(comment_list)
            print("No of likes for the post: %d" % (maximum))
            index = comment_list.index(maximum)
            post_index = post_id_list[index]
            print("Most liked post-id: %s" % (post_index))
            image_name = user_name + str(post_index) + '.jpg'
            image_url = user_info['data'][index]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)  # -----saving the user's latest post-----#
            original = Image.open(image_name)
            original.show()
            print("Your image has been successfully saved..")

        else:
            print("No info exist")
    else:
        print("Incorrect code..")

